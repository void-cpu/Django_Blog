# Generated by Django 3.1.6 on 2021-02-13 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20210213_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment_status',
        ),
    ]
