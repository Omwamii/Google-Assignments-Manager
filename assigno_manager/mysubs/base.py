import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



class Base():
    """ Oauth implementation for logins & API resources initialization"""
    creds = None
    flow = None
    data = None
    # _id = 114502058831176393158

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
      "https://www.googleapis.com/auth/classroom.coursework.me",
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