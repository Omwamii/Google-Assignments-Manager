from django.shortcuts import render



def index(request):
    """ Index page """
    return render('index.html')
