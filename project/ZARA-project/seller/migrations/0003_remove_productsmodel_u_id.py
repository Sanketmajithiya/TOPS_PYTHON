# Generated by Django 5.0.6 on 2024-06-29 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_productsmodel_u_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='u_id',
        ),
    ]
