from django.urls import path
from.import views
from . views import github

urlpatterns = [
    path('api/', views.github, name='github'),
]
