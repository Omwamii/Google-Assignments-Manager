""" api function-based views """
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .app import App
from .models import MarksAsDone

"""
Test units
{
        "id": "640286398164",
        "name": "Group1_CSC_319_October2023_Feb2024"
    },
    {
        "id": "634082930362",
        "name": "CSC315 Distributed Systems, 2023-2024"
    },
    {
        "id": "632230740983",
        "name": "CSC311G1-G2-YR2023-2024 ANALYSIS AND DESIGN OF ALGORTHMS"
    },
    {
        "id": "632004324252",
        "name": "Computer Graphics CSC314"
    },
    {
        "id": "631842527791",
        "name": "CSC 316 Introduction to organizations and management"
    },
    {
        "id": "346224049561",
        "name": "CSC 318 - 2023/2024"
    }
"""

app = App()  # App instance with auth & classroom resources

@api_view(['GET'])
def coursework(_, unit_id):
    """ Returns coursework of a unit
        Required: unit ID
    """
    return Response(app.get_coursework(unit_id))


@api_view(['GET'])
def submissions(_, unit_id):
    """ Returns student's submission for a unit's coursework
        Required: Unit ID
    """
    return Response(app.get_unit_submissions(unit_id))


@api_view(['GET'])
def assignments(_):
    """ Return pending assignments """
    return Response(app.get_pending_work())


@api_view(['GET'])
def assignment(_, unit_id, work_id):
    """ Get an assignment"""
    return Response(app.get_assignment(unit_id, work_id))

@api_view(['GET'])
def units(_):
    """ Course units which the student has enrolled """
    return Response(app.get_courses())


@api_view(['POST'])
def submit_assignment(request):
    """ View to Submit an assignment
        will need drive api &
        Get ids from request frontend & use ids to submit collection of files 
    """
    file_s = request.FILES.getlist('file')
    print(f"File(s) {file_s}")
    for file in file_s:
        # print(f"name: {file.name}")
        # print(f"Mime type: {file.content_type}")
        app.upload_file(file.name, file.content_type, file.read())
    return Response('success!!')


@api_view(['POST'])
def add_to_calendar(_):
    """ Add assignment due date to calendar """
    pass


@api_view(['GET'])
def get_notifications(_, unit_id):
    """ Get actions needed (notifs) """
    return Response(app.get_notifications(unit_id))

@api_view(['GET'])
def undo_submit(_):
    """ reclaim work submission """
    # use courswork reclaim() fn


@api_view(['GET'])
def grades(_, unit_id):
    """ get grades for a unit"""
    return Response(app.get_grades(unit_id))


@api_view(['GET'])
def stats(_):
    """ Get average grades per unit for chart display"""
    return Response(app.get_unit_avg())

@api_view(['POST'])
def markdone(request):
    """ Mark an assignment as done
        Work without due time has to be marked as done to take them off the list of due work
    """
    work_id = request.POST.get('id')
    course_id = request.POST.get('course_id')
    work_marked_obj = MarksAsDone.objects.create(work_id=work_id, course_id=course_id)
    if work_marked_obj:
        return Response({'message': 'Work marked as done successfully', 'error': False})
    return Response({'message': 'Error marking work as done', 'error': True})