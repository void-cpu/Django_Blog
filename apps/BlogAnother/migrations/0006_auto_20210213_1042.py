# Generated by Django 3.1.6 on 2021-02-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAnother', '0005_auto_20210213_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=100, verbose_name='内容'),
        ),
    ]
