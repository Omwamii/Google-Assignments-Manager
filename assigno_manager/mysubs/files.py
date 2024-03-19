""" App functionality for file management"""
from .course import Course
from os import remove as delete_file
from googleapiclient.http import MediaFileUpload
from google.protobuf.json_format import MessageToJson
import json


class Files(Course):
    """ Class to manage classroom files actions """
    def work_was_turned_in(self, course_id, course_work_id):
      """ Check if student had turned in work
          Return true if work was turned in else false
      """
      sub = (self.service.courses().courseWork().studentSubmissions().list(
        courseId=course_id,
        courseWorkId=course_work_id
        ).execute()).get('studentSubmissions')[0]
      # https://developers.google.com/classroom/reference/rest/v1/SubmissionState 
      # ^ docs on diff submission states
      if sub.get('state') == 'TURNED_IN':
        return True
      return False

    def upload_file(self, file_name, mime_type, file_data):
       """ Upload a file to Google Drive."""
       file_metadata = {'name': file_name}
       # issue: getting absolute file path from frontend impossible
       # since file selection not linked to django, get uploaded file & write
       # then delete after upload
       f = open(file_name, 'wb')
       f.write(file_data)
       f.close()
       media = MediaFileUpload(file_name, mimetype=mime_type, resumable=True)
       file = self.drive.files().create(
         body=file_metadata, media_body=media, fields='id').execute()
       delete_file(file_name) # delete file after upload
       print(f"Uploaded file with ID: {file.get('id')}")
       return file.get('id')

    def get_file(self, file_id: str) -> str:
      """ Get file info from drive """
      if not file_id:
        return {}
      return self.drive.files().get(fileId=file_id, fields='id,name,thumbnailLink,webViewLink').execute()
    
   
    
    def add_attachment(self, drive_file_id, course_id, course_work_id):
      """ Add a file/link attachment to an assignment submission """
    #   drive_file = self.get_file(drive_file_id)
      submission_id = self.get_submission_id(course_id, course_work_id)
      print(f"Submission id: {submission_id}")
      request_body = {
        'addAttachments': [
          {
            'driveFile': {
              'id': drive_file_id
            }
          }
        ]
      }
      sub = self.service.courses().courseWork().studentSubmissions().modifyAttachments(
        courseId=course_id,
        courseWorkId=course_work_id,
        id=submission_id,
        body=request_body
      ).execute()
      print(f" result of adding attachment: {sub}")
      return sub

    def turn_in_assignment(self, course_id, course_work_id):
      """ Turn in an assignment 
          Return empty body as response if successful
      """
      submission_id = self.get_submission_id(course_id, course_work_id)
      res = self.service.courses().courseWork().studentSubmissions().turnIn(
        courseId=course_id,
        courseWorkId=course_work_id,
        id=submission_id
      ).execute()
      print(f"result of turning in assignment: {res}")
      return res
    
    def unsubmit_assignment(self, course_id, course_work_id):
      """ Unsubmit an assignment 
          Returns empty body as response if successful
      """
      submission_id = self.get_submission_id(course_id, course_work_id)
      res = self.service.courses().courseWork().studentSubmissions().reclaim(
        courseId=course_id,
        courseWorkId=course_work_id,
        id=submission_id
      ).execute()
      print(f"result of unsubmitting assignment: {res}")
      return res
