""" api function-based views """
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .app import App
from .models import MarksAsDone

app = App()  # App instance with auth & classroom resources


#TODO add concurent processes to reduce get_assignments() time

@api_view(['GET'])
async def coursework(_, unit_id):
    """ Returns coursework of a unit
        Required: unique unit ID
    """
    return Response(app.get_coursework(unit_id))

@api_view(['GET'])
async def submissions(_, unit_id):
    """ Returns student's submission for a unit's coursework
        Required: Unit ID
    """
    return Response(app.get_unit_submissions(unit_id))

@api_view(['GET'])
async def submission(_, unit_id, work_id):
    return Response(app.get_submission_files(unit_id, work_id))

@api_view(['GET'])
async def assignments(_):
    """ Return pending assignments """
    return Response(app.get_pending_work())

@api_view(['GET'])
async def assignment(_, unit_id, work_id):
    """ Get an assignment"""
    return Response(app.get_assignment(unit_id, work_id))

@api_view(['GET'])
async def units(_):
    """ Course units which the student has enrolled """
    return Response(app.get_courses())


@api_view(['POST'])
async def submit_assignment(request, course_id, work_id):
    """ View to Submit an assignment
        will need drive api &
        Get ids from request frontend & use ids to submit collection of files 
    """
    file_s = request.FILES.getlist('file')
    if app.work_was_turned_in(course_id, work_id):
        app.unsubmit_assignment(course_id, work_id)
    for file in file_s:
        # upload  file to google drive & get file id
        drive_file_id = app.upload_file(file.name, file.content_type, file.read())
        # add file as attachment to submission
        app.add_attachment(drive_file_id, course_id, work_id)
    return Response(app.turn_in_assignment(course_id, work_id)) # turn in work


@api_view(['GET'])
async def unsubmit_assignment(_, course_id, work_id):
    """ Unsubmit an assignment """
    return Response(app.unsubmit_assignment(course_id, work_id))

@api_view(['GET'])
async def get_notifications(_, unit_id):
    """ Get actions needed (notifs) """
    return Response(app.get_notifications(unit_id))

@api_view(['GET'])
async def grades(_, unit_id):
    """ get grades for a unit"""
    return Response(app.get_grades(unit_id))


@api_view(['GET'])
async def stats(_):
    """ Get average grades per unit for chart display"""
    stats = app.get_unit_avg()
    stats_dict = dict()
    for stat in stats:
        for key, val in stat.items():
            stats_dict[key] = val
    return Response(stats_dict)

@api_view(['POST'])
async def mark_as_done(_, unit_id, work_id):
    """ Mark an assignment as done
        Work without due time has to be marked as done to take them off the list of due work
    """
    work_marked_obj = MarksAsDone.objects.create(work_id=work_id, course_id=unit_id)
    if work_marked_obj:
        return Response({'message': 'Work marked as done successfully', 'error': False})
    return Response({'message': 'Error marking work as done', 'error': True})
