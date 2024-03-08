""" api function-based views """
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .auth import App

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


@api_view(['GET'])
def submit_assignment(_):
    """ View to Submit an assignment
        will need drive api &
        Get ids from request frontend & use ids to submit collection of files 
    """
    # file = app.upload_file()
    file = app.get_file('1wiO5zDrWsSw5BXhjx1WCLeuYp9iR4ztY')
    # after adding files to drive, store added files to list, use ids to retrieve files & 
    # to attachments object 
    # Assignment submission file
    data = {"driveFile": {'id': file.get('id', None),
            'title': file.get('name', None),
            'alternateLink': file.get('webViewLink', None),
            'thumbnailUrl': file.get('thumbnailLink', None)}
            }
    # For file download request webContentLink from file metadata (through app instance)
    return Response(data)


@api_view(['POST'])
def add_to_calendar(_):
    """ Add assignment due date to calendar """
    pass


@api_view(['GET'])
def get_notifications(_, unit_id):
    """ Get actions needed (notifs) """
    return Response(app.get_notifications(unit_id))

@api_view(['POST'])
def send_private_message(_):
    """ Send lectuter private message.
        Attach coursework/Assignment context? 
    """
    pass


@api_view(['GET'])
def undo_submit(_):
    """ reclaim work submission """
    # use courswork reclaim() fn


@api_view(['GET'])
def grades(_, unit_id):
    """ get grades for a unit"""
    return Response(app.get_grades(unit_id))

