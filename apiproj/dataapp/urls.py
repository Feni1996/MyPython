from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('f/', views.feedbackview.as_view(), name='feedback'),
]
