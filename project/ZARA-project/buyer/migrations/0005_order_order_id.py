# Generated by Django 5.0.4 on 2024-06-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
