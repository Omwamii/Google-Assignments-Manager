from django.db import models

# Create your models here.
class Student(models.Model):
    """ Student model"""
    # name
    # year of study?
    # course
    pass

class Assignment(models.Model):
    """ Active assignments for user"""
    # Unit / course
    # lecturer
    # Due date
    # points / marks
    pass

class EnrolledUnit(models.Model):
    """ Units enrolled by student """
    # unit name
    # unit code
    # unit lecturer(s)

class Submission(models.Model):
    """ Assignments submitted by students """
    # Assignment reference
    # submission date
    # submission grade
    pass

class Notif(models.Model):
    """ Notifications? """
    # description
    # link: action
    pass

class Lecturer(models.Model):
    """ Add lecturers? 
        Purpose: ability to send private message on classroom
    """
    pass