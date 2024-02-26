# from django.db import models

# # Create your models here.
# class Assignment(models.Model):
#     """ Active assignments for user"""
#     # Unit / course -> course id (int)?
#     # lecturer
#     # Due date
#     # points / marks
#     # submitted -> boolean
#     # must be connected to enrolled units
#     pass

# class EnrolledUnit(models.Model):
#     """ Units enrolled by student """
#     # unit name
#     # unit code
#     # unit lecturer(s)
#     # connected ref student (one to many)

# class Submission(models.Model):
#     """ Assignments submitted by students """
#     # student reference
#     # Assignment reference (file)
#     # submission date
#     # due time
#     # submission grade
#     pass

# class Notif(models.Model):
#     """ Notifications? """
#     # description
#     # link: action
#     pass

# class Lecturer(models.Model):
#     """ Add lecturers? 
#         Purpose: ability to send private message on classroom
#     """
#     pass
