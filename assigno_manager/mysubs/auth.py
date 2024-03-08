#!/usr/bin/env python3
""" Module to implement O-Auth for the app
"""
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from datetime import datetime
from typing import List
from .models import Notification



class App:
    """ Oauth implementation for logins & API resources initialization"""
    creds = None
    flow = None
    data = None
    _id = 114502058831176393158

    # add memoization
    # If modifying these scopes, delete the file token.json.
    _SCOPES = [
      "https://www.googleapis.com/auth/classroom.courses.readonly",
      "https://www.googleapis.com/auth/classroom.announcements",
      "https://www.googleapis.com/auth/classroom.course-work.readonly",
      "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
      "https://www.googleapis.com/auth/classroom.announcements.readonly",
      "https://www.googleapis.com/auth/classroom.addons.student",
      "https://www.googleapis.com/auth/classroom.push-notifications",
      "https://www.googleapis.com/auth/userinfo.profile",
      "https://www.googleapis.com/auth/drive.file"
      ]


    def __init__(self):
      """ Initialize Oauth login for each instance (self.creds)
          Avail service to fetch resources e.g courses, assignments (self.service)
      """
      if os.path.exists("token.json"):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        self.creds = Credentials.from_authorized_user_file('token.json', self._SCOPES)

      if not self.creds or not self.creds.valid:
        if self.creds and self.creds.expired and self.creds.refresh_token:
          self.creds.refresh(Request())
        else:
            # credentials file was downloaded to root from google cloud console credentials
            self.flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self._SCOPES)
            self.creds = self.flow.run_local_server(port=8080)
        
        with open("token.json", "w") as token:
          token.write(self.creds.to_json())

      try:
        # setup google classroom api
        self.service = build("classroom", "v1", credentials=self.creds)
      except HttpError as error:
        # Error with classroom API
        print(f"Classroom API error: {error}")
      else:
        # calling classroom API to fetch course data
        self.data = self.service.courses().list().execute()

      try:
        # setup google drive api
        self.drive = build("drive", "v3", credentials=self.creds)
      except HttpError as error:
        # Error with google drive api
        print(f"Drive API error: {error}")
    
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
        if not res.get('assignmentSubmission'):
          # Could be a group submission, not your submission
          continue

        data = {'id': res['id'], 'title': work.get('title'), 'link': work.get('alternateLink'),
               'maxPoints': work.get('maxPoints'), 'grade': res.get('assignedGrade'),
               'submission': res.get('assignmentSubmission')
               }
        submissions.append(data)
      return submissions
    
    def do_submit(self, course_id: int, course_work_id: int, attachments: List[dict]) -> str:
      """ Submit an assignment with attachments"""
      return self.service.courses().courseWork().studentSubmissions().modifyAttachments(courseId=course_id,
                                                                                        courseWorkId=course_work_id,
                                                                                        id=self._id).execute()
    
    def upload_file(self):
      """ Upload a file to google drive """
      file_metadata = {"title": "download.jpeg"}
      media = MediaFileUpload("download.jpeg", mimetype="image/jpeg")
      # pylint: disable=maybe-no-member
      # file = (
      #    self.drive.files().create(body=file_metadata, media_body=media, fields="id, title, alternateLink, thumbnailUrl").execute()
      # )
      file = self.drive.files().list().execute()
      return file

    def get_file(self, file_id: str) -> str:
      """ Get file from drive """
      if not file_id:
        return {}
      return self.drive.files().get(fileId=file_id, fields='id,name,thumbnailLink,webViewLink').execute()
    
    def get_pending_work(self):
      """ Return pending assignments for all units """
      courses = self.get_courses()
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
          pending_work = {
            'id': work['id'], 'unit': unit_name, 'title': work.get('title'), 'classLink': work['alternateLink'],
            'points': work.get('maxPoints'), 'dueTime': d_time
          }
          if not d_time:
            # work does not have due date
            pending.append(pending_work)
          else:
            if d_time > datetime.now():
              # deadline for assignment not reached yet
              pending.append(pending_work)
      return pending
    
    def get_assignment(self, unit_id: int, course_work_id: int) -> str:
      """ Return a specific assignment """
      test_d = {
        'year': 2023,
        'month': 11,
        'day': 29,
        'hour': 10,
        'minute': 30
      }
      test_date = datetime(**test_d)
  
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
        if test_date > due_date:
          time_remaining += 'Deadline passed by'
          passed_by = test_date - due_date

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
            # minutes_passed = 135
            hrs = int(minutes_passed / 60)
            minutes_passed = int(minutes_passed % 60)
            time_remaining += f" {hrs} hrs,"
          time_remaining += f" {minutes_passed} minutes"
        else:
          rem_time = due_date - test_date
          if rem_time.days > 0:
            time_remaining += f"{rem_time.days} days"
          minutes_remaining = int(rem_time.total_seconds() // 60)
          time_remaining += f"{minutes_remaining} minutes"
      else:
        time_remaining = 'No due time'
      data = {'id': work['id'], 'courseId': work['courseId'], 'title': work['title'],
              'description': work['description'], 'maxPoints': work['maxPoints'],
              'time': time_remaining}
      return data
    
    def get_grades(self, course_id):
      """ Returns grades for a certain unit"""
      c_work = self.get_coursework(course_id)
      grades = list()
      for work in c_work:
        sub = self.get_submission(course_id, work.get('id', None))
        res = {'title': work.get('title'), 'link': work.get('alternateLink'),
               'maxPoints': work.get('maxPoints'), 'grade': sub.get('assignedGrade')
               }
        grades.append(res)
      return grades

if __name__ == "__main__":
  app = App()  # For testing to separate auth errors from app errors