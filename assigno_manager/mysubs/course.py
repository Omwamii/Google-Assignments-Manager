#!/usr/bin/env python3
""" Module with app functionalities for course data manipulation
"""
import os.path
from os import environ as env
import json
from datetime import datetime
from typing import List
# from .models import Notification
from .regex import get_course_code
from .base import Base
from .models import MarksAsDone

class Course(Base):
    """ App functionalities """
    def get_courses(self):
      """ Return all courses student is enrolled in """
      # return self.data.get('courses', [])
      courses = self.data.get('courses', [])
      units = list()
      for course in courses:
        if course['courseState'] != 'ACTIVE':
          # archived courses
          continue
        data = {'id': course['id'], 'name': course['name']}
        units.append(data)
      return units

    
    def get_coursework(self, course_id: int) -> str:
      """ Return unit's coursework
          course_id: id for unit 
      """
      # Add function to get materials (addons) on a coursework 
      c_work = self.service.courses().courseWork().list(courseId=course_id).execute().get('courseWork')
      if not c_work:
        return []
      return c_work
    
    def get_notifications(self, course_id: int) -> str:
      """ Return announcements on a course

          Get notifications & save to database, to avoid refetching, fetch only first
          notification after initial bulk fetch & try to get in db?
      """
      notifs = self.service.courses().announcements().list(courseId=course_id).execute().get('announcements')
      notifications = list()
      format = "%Y-%m-%dT%H:%M:%S.%fZ"
      for notif in notifs:
        now = datetime.utcnow()
        then = datetime.strptime(notif['updateTime'], format)
        time_passed = now - then
        minutes_passed = time_passed.total_seconds() // 60
        if time_passed.days:
          time_str = str(time_passed.days) + ' days ago'
        else:
          time_str = minutes_passed + ' minutes ago'
        notif_obj = {'id': notif['id'], 'courseId': notif['courseId'], 'text': notif['text'],
                     'time': time_str}
        notifications.append(notif_obj)
      return notifications
    

    def get_submission(self, course_id: int, coursework_id: int) -> str:
      """ Return a submission for a coursework """
      # possible issue: studentSubmisions being an array, above code assumes 
      # there's always one submission for a coursework assigned a grade..

      return self.service.courses().courseWork().studentSubmissions().list(
        courseId=course_id,
        courseWorkId=coursework_id
      ).execute().get('studentSubmissions')[0]
    
    def get_unit_submissions(self, course_id: int) -> str:
      """ Return student submissions for a unit
          course_id: unit ID
          course_work_id: ID for specific coursework item
      """
      coursework = self.get_coursework(course_id)
      submissions = list()
      for work in coursework:
        res = self.get_submission(course_id, work['id'])
        print(res)
        if not res.get('assignmentSubmission'):
          # Could be a group submission, not your submission
          # continue
          print('No submission')

        data = {'id': res['id'], 'title': work.get('title'), 'link': work.get('alternateLink'),
               'maxPoints': work.get('maxPoints'), 'grade': res.get('assignedGrade'),
               'submission': res.get('assignmentSubmission'), 'courseWorkId': work['id'],
               'courseId': course_id
               }
        submissions.append(data)
      return submissions

    def get_pending_work(self):
      """ Return pending assignments for all units """
      courses = self.data.get('courses', [])
      pending = list()
      for course in courses:
        if course['courseState'] != 'ACTIVE':
          continue
        unit_name = course['name']
        c_work = self.get_coursework(course['id'])
        for work in c_work:
          if work.get('materials'):
            if work['materials'][0].get('form'):
              # API does not support form submission
              continue 
          d_time = work.get('dueDate', None)
          if d_time:
             d_time = datetime(d_time['year'], d_time['month'], d_time['day'])
          else:
            # Before appending work as due, check if had been marked as done
            try:
              _ = MarksAsDone.objects.get(work_id=work['id'], course_id=course['id'])
            except Exception:
              pass
            else:
              print('Marked as done')
              continue
          print(f"Mod mode {work.get('submissionModificationMode')}")
          pending_work = {
            'id': work['id'], 'unit': unit_name, 'title': work.get('title'), 'classLink': work['alternateLink'],
            'points': work.get('maxPoints'), 'dueTime': d_time if d_time else ' No due time', 'courseId': course['id']
          }
          if not d_time:
            # work does not have due date
            pending.append(pending_work)
          else:
            if d_time > datetime.now():
              # deadline for assignment not reached yet
              pending.append(pending_work)
            # issue: API does not provide fnality to check late work policy
            # so can't append work past due but submissions allowed
      return pending
    
    def get_assignment(self, unit_id: int, course_work_id: int) -> str:
      """ Return a specific assignment
          Fav part hehe
      """
      today_t = datetime.now()
  
      work = self.service.courses().courseWork().get(
        courseId=unit_id, id=course_work_id).execute()
      if work.get('dueDate'):
        date = work.get('dueDate')
        if work.get('dueTime'):
           time = work.get('dueTime')
           time = {'hour': time['hours'], 'minute': time['minutes']}
           date.update(time)

        due_date = datetime(**date)
        time_remaining = ""
        if today_t > due_date:
          time_remaining += 'Deadline passed by'
          passed_by = today_t - due_date

          if passed_by.days > 0:
            time_remaining += f" {passed_by.days} days,"

          if (passed_by.total_seconds() / 3600) > 24:
            # assignment's deadline passed past one day (3600 secs in 1hr)
            # 86400 - number of seconds in a day. divide to find number of days 
            # Then subtraction from days to get fraction of day remaining
            # Fraction of day then converted to minutes by (24 * 60)
            minutes_passed = ((passed_by.total_seconds() / 86400) - passed_by.days) * (24 * 60)
          else:
            minutes_passed = passed_by.total_seconds() / 60
          if minutes_passed > 60:
            hrs = int(minutes_passed / 60)
            minutes_passed = int(minutes_passed % 60)
            time_remaining += f" {hrs} hrs,"
          time_remaining += f" {minutes_passed} minutes"
        else:
          rem_time = due_date - today_t
          if rem_time.days > 0:
            time_remaining += f"{rem_time.days} days"
          minutes_remaining = int(rem_time.total_seconds() // 60)
          time_remaining += f"{minutes_remaining} minutes"
      else:
        time_remaining = 'No due time'
      data = {'id': work.get('id'), 'courseId': work['courseId'], 'title': work.get('title'),
              'description': work.get('description'), 'maxPoints': work.get('maxPoints'),
              'time': time_remaining}
      return data
    
    def get_grades(self, course_id):
      """ Returns grades for a certain unit"""
      c_work = self.get_coursework(course_id)
      grades = list()
      for work in c_work:
        sub = self.get_submission(course_id, work.get('id', None))
        res = {'id': work.get('id'), 'title': work.get('title'), 'link': work.get('alternateLink'),
               'maxPoints': work.get('maxPoints'), 'grade': sub.get('assignedGrade')
               }
        grades.append(res)
      return grades
    
    def get_unit_avg(self):
      """ Get average grades per unit
          Issue: most units have unassigned grades, for display
          sample data is used and can be changed by using env variables
      """
      avg_grades = list()
      if env.get('USE_CHART_DATA') == 'REAL':
        # use real student data
        units = self.get_courses()
        for unit in units:
          avg, work_count = 0, 0
          grades = self.get_grades(unit['id'])
          for grade in grades:
            if grade['grade'] is None:
              # work not assigned a grade
              continue
            avg += ( grade['grade'] / grade['maxPoints']) * 100 # get percentage
            work_count += 1
          if avg != 0:
            avg = int(avg / work_count)
            data = {'unit': get_course_code(unit['name']), 'avg': avg}
            avg_grades.append(data)
      else:
        # use dummy data for display test, use USE_CHART_DATA=REAL to view real data
        with open('mysubs/data/stats.json', 'r') as f:
          stats = json.load(f)
          for key, val in stats.items():
            data = {'unit': get_course_code(key), 'avg': val}
            avg_grades.append(data)
      return avg_grades
