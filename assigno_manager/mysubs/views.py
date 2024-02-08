from django.shortcuts import render_template



def index(request):
    """ Index page """
    return render_template('index.html')


def submit(request):
    """ Submit an assignent """


def get_stats(request):
    """ Get grades on assignmnents """


def download_submission(request):
    """ Download a submission had submitted """
