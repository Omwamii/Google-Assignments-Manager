import os.path
import os
import socket
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from psutil import process_iter
from signal import SIGTERM # or SIGKILL


class Base():
    """ O-auth implementation for logins & API resources initialization. """
    creds, flow, data = (None, None, None)

    # If modifying these scopes, delete the file token.json and restart authoration
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
        # The file token.json stores the user's access and refresh tokens, and is.
        # created automatically when the authorization flow completes for the first
        # time.
        self.creds = Credentials.from_authorized_user_file('token.json', self._SCOPES)

      if not self.creds or not self.creds.valid:
        if self.creds and self.creds.expired and self.creds.refresh_token:
            try:
                self.creds.refresh(Request())
            except Exception:
                os.remove('token.json')
                # temp sln for refresh token error
                try:
                    _kill_process(8080)
                except Exception:
                    pass

                self.flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self._SCOPES)
                self.creds = self.flow.run_local_server(port=8080, access_type='offline', prompt='consent')
                _kill_process(8080)
        else:
            # credentials file was downloaded to root from google cloud console credentials
            try:
                _kill_process(8080)
            except Exception:
                pass

            self.flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self._SCOPES)
            self.creds = self.flow.run_local_server(port=8080, access_type='offline', prompt='consent')
            _kill_process(8080)

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


def _kill_process(port_number: int) -> None:
    """ Kill process """
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port_number:
                proc.send_signal(SIGTERM) # or SIGKILL
