# Q.1 Q.1 Why Django should be used for web-development? Explain how you can create a project in Django? 
""" 
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel

To create a project in Django, follow these steps:


(1)create vertiual env for 'project-name' project:-
python -m venv

(2)activate your vertiual env:-
env-name\Scripts\activate

(3)create requirements.txt file
env-name>type nul > requirements.txt

(4)check Python 3.x.y version require for django==5.0.0
> python --version

(5)Install Django: First, make sure you have Python installed on your system. Then, install Django using pip:
pip install django

(6)create django project
django-admin startproject project-name .

(7)create django app
python manage.py startapp app-name

(8)Migrate Database: Once you've defined your models, run migrations to create database tables based on your model definitions:
python manage.py makemigrations

(9)migrate table
python manage.py migrate

(10)run local server
python manage.py runserver

(11)craete super user
python manage.py createsuperuser

Start Developing: You're now ready to start developing your Django project! Use the Django documentation and other resources to guide you through the process of building your web application.

"""