# Generated by Django 3.0.8 on 2020-09-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20200917_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=254, unique=True),
        ),
    ]
