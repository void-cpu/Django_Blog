# Generated by Django 3.1.6 on 2021-02-13 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAnother', '0008_auto_20210213_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='Creation_time',
        ),
    ]
