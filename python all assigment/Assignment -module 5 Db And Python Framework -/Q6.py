# Q.6 Mention what command line can be used to load data into Django?
"""
To load data into Django you have to use the command line Django-admin.py loaddata. The command line will searches the data and loads the contents of the named fixtures into the database


To load data into a Django project, you can use the loaddata command provided by Django's manage.py utility. This command is used to load data from fixture files into the database. Fixture files can be in various formats such as JSON, XML, or YAML, and they contain serialized data for Django models.

1.Here's how you can use the loaddata command:
python manage.py loaddata <fixture_name>

2.where <fixture_name> is the name of the fixture file you want to load.

For example, if you have a JSON fixture file named initial_data.json, you would use the following command to load its data into the database:

python manage.py loaddata initial_data.json



"""