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
    return Response({'data': app.get_coursework(632004324252)})


@api_view(['GET'])
def assignments(request):
    """ Return pending assignments """
    pass


@api_view(['GET'])
def units(request):
    """ Course units which the student has enrolled """
    return Response({'data': app.get_courses()})


@api_view(['POST'])
def submit_assignment(request):
    """ View to Submit an assignment """
    pass


@api_view(['POST'])
def add_to_calendar(request):
    """ Add assignment due date to calendar """
    pass


@api_view(['GET'])
def get_notifications(request):
    """ Get actions needed (notifs) """
    return Response({'data': app.get_notifications(632004324252)})

@api_view(['POST'])
def send_private_message(request):
    """ Send lectuter private message.
        Attach coursework/Assignment context? 
    """
    pass
