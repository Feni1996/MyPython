from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from . serializer import feedbackserializer, personserializer
from . models import feedback, Person
from rest_framework import viewsets

class feedbackview(generics.ListAPIView):
    queryset = feedback.objects.all()
    serializer_class = feedbackserializer
    
class feedbackviewsets(viewsets.ModelViewSet):
    queryset = feedback.objects.all()
    serializer_class = feedbackserializer

class personviewsets(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = personserializer