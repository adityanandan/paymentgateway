# Generated by Django 3.0.8 on 2020-09-17 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20200917_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='paid',
        ),
    ]
