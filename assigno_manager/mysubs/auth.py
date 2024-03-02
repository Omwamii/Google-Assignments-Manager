#!/usr/bin/env python3
""" Module to implement O-Auth for the app
"""
import os.path
import logging

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




class App:
    """ Oauth implementation for logins & API resources initialization"""
    creds = None
    flow = None
    data = None

    # add memoization
    # If modifying these scopes, delete the file token.json.
    SCOPES = [
      "https://www.googleapis.com/auth/classroom.courses.readonly",
      "https://www.googleapis.com/auth/classroom.announcements",
      "https://www.googleapis.com/auth/classroom.course-work.readonly",
      "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
      "https://www.googleapis.com/auth/classroom.announcements.readonly",
      "https://www.googleapis.com/auth/classroom.addons.student",
      "https://www.googleapis.com/auth/classroom.push-notifications",
      "https://www.googleapis.com/auth/userinfo.profile"]


    def __init__(self):
      """ Initialize Oauth login for each instance (self.creds)
          Avail service to fetch resources e.g courses, assignments (self.service)
      """
      if os.path.exists("token.json"):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)

      if not self.creds or not self.creds.valid:
        if self.creds and self.creds.expired and self.creds.refresh_token:
          self.creds.refresh(Request())
        else:
            # credentials file was downloaded at root from google cloud console credentials
            self.flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
            self.creds = self.flow.run_local_server(port=8080)
        
        with open("token.json", "w") as token:
          token.write(self.creds.to_json())

      try:
        self.service = build("classroom", "v1", credentials=self.creds)
      except HttpError as error:
        logging.exception(f"An error occured: {error}")
      else:
        # calling classroom API to fetch course data
        self.data = self.service.courses().list().execute()
    
    def get_courses(self):
      """ Return all courses student is enrolled in """
      return self.data.get('courses', [])

    
    def get_coursework(self, course_id):
      """ Return unit's coursework
          course_id: id for unit 
      """
      # Add function to get materials (addons) on a coursework 
      return self.service.courses().courseWork().list(courseId=course_id).execute()
    
    def get_notifications(self, course_id):
      """ Return announcements on a course"""
      return self.service.courses().announcements().list(courseId=course_id).execute()

if __name__ == "__main__":
  app = App()  # For testing to separate auth errors from app errors
