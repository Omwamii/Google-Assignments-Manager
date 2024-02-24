from django.shortcuts import render

from rest_framework import viewsets
# import serializer
from .serializers import Serializer
# import model

class AssignmentsView(viewsets.ModelViewSet):
    """ View for Assignments: API use"""
    serializer_class = Serializer