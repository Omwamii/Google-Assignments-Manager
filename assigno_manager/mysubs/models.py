from django.db import models

# most Models not necessary -> Classroom API utilized for data

# class Notification(models.Model):
#     """ Notifications on google classroom
#         Reason: enable identifying notification as 'read' or seen
#         since API not providing the option
#     """
#     id = models.CharField(max_length=50, primary_key=True)
#     courseId = models.CharField(max_length=50)
#     text = models.TextField()
#     publish_date = models.DateField()
#     seen = models.BooleanField(default=False)