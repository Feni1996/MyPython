from rest_framework import serializers
from . models import feedback, Person

class feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model= feedback
        fields = '__all__'
        
class personserializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = '__all__'