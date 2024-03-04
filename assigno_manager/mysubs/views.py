""" api function-based views """
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .auth import App


app = App()  # App instance with auth & classroom resources

@api_view(['GET'])
def coursework(request):
    """ Returns coursework of a unit
        Required: unit ID
    """
    return Response(app.get_coursework(632004324252))


@api_view(['GET'])
def submission(request):
    """ Returns student's submission for a unit's coursework
        Required: Unit ID
    """
    return Response(app.get_submission(632004324252, 641698591232))


@api_view(['GET'])
def assignments(request):
    """ Return pending assignments """
    return Response(app.get_pending_work())


@api_view(['GET'])
def units(request):
    """ Course units which the student has enrolled """
    return Response(app.get_courses())


@api_view(['GET'])
def submit_assignment(request):
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
def add_to_calendar(request):
    """ Add assignment due date to calendar """
    pass


@api_view(['GET'])
def get_notifications(request):
    """ Get actions needed (notifs) """
    return Response(app.get_notifications(632004324252))

@api_view(['POST'])
def send_private_message(request):
    """ Send lectuter private message.
        Attach coursework/Assignment context? 
    """
    pass


@api_view(['GET'])
def undo_submit(request):
    """ reclaim work submission """
    # use courswork reclaim() fn


@api_view(['GET'])
def grades(request):
    """ get grades for a unit"""
    return Response(app.get_grades(632004324252))

