# Generated by Django 2.2.4 on 2019-08-15 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundimages',
            name='updated',
        ),
    ]