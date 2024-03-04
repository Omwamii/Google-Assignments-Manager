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
            # credentials file was downloaded at root from google cloud console credentials
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
      return self.data.get('courses', [])

    
    def get_coursework(self, course_id: int) -> str:
      """ Return unit's coursework
          course_id: id for unit 
      """
      # Add function to get materials (addons) on a coursework 
      return (self.service.courses().courseWork().list(courseId=course_id).execute()).get('courseWork')
    
    def get_notifications(self, course_id: int) -> str:
      """ Return announcements on a course

          Get notifications & save to database, to avoid refetching, fetch only first
          notification after initial bulk fetch & try to get in db?
      """
      notifs = self.service.courses().announcements().list(courseId=course_id).execute().get('announcements')
      notifications = list()
      for notif in notifs:
        notif_obj = {'id': notif['id'], 'courseId': notif['courseId'], 'text': notif['text'],
                     'time': notif['updateTime']}
        notifications.append(notif_obj)
      return notifications

    
    def get_submission(self, course_id: int, course_work_id: int) -> str:
      """ Return student submissions for a unit
          course_id: unit ID
          course_work_id: ID for specific coursework item
      """
      return (self.service.courses().courseWork().studentSubmissions().list(courseId=course_id,
                                                                         courseWorkId=course_work_id)
                                                                         .execute()).get('studentSubmissions')
    
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
        c_work = self.get_coursework(course['id'])
        for work in c_work.get('courseWork', []):
          if work.get('materials'):
            if work['materials'][0].get('form'):
              continue # API does not support form submission
          d_time = work.get('dueDate', None)
          if not d_time:
            pending.append(work) # work does not have due date
            due_time = None
          else:
            due_time = datetime(d_time['year'], d_time['month'], d_time['day'])
          if due_time and due_time > datetime.now():
            # deadline for assignment not reached yet
            pending.append(work)
      return pending
    
    def get_grades(self, course_id):
      """ Returns grades for a certain unit"""
      c_work = self.get_coursework(course_id)
      grades = list()
      for work in c_work:
        sub = self.get_submission(course_id, work.get('id', None))
        res = {'title': work.get('title'), 'link': work.get('alternateLink'),
               'maxPoints': work.get('maxPoints'), 'grade': sub[0].get('assignedGrade'),
               'submission': sub[0]['assignmentSubmission'].get('attachments')}
        grades.append(res)
      return grades

if __name__ == "__main__":
  app = App()  # For testing to separate auth errors from app errors
