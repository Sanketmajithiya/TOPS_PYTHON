# Q.4 What is Django URLs?make program to create django urls
"""
1. Project-Level URLs (urls.py):
Create a file named urls.py in the same folder as the views.py file, and type this code in it:

Create a Django project using the django-admin startproject command.
In the project directory, locate the urls.py file, which serves as the main URL configuration file for the project.
Define URL patterns in this file using the urlpatterns list. Each URL pattern is a tuple containing a regex pattern and the corresponding view function or class.
Optionally, use the include() function to include URL configurations from other modules.

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]

"""