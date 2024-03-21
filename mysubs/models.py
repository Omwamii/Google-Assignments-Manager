from django.db import models

# most Models not necessary since Classroom API is utilized for data

class MarksAsDone(models.Model):
    """ Enable marking work without due time as done
        Work without due time is assigned as pending work in app
    """
    work_id = models.CharField(max_length=50, primary_key=True)
    course_id = models.CharField(max_length=50)