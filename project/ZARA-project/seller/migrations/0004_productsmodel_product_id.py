# Generated by Django 5.0.6 on 2024-06-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_remove_productsmodel_u_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='product_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]