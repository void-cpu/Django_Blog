# Generated by Django 3.1.6 on 2021-02-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_User', '0002_auto_20210212_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodels',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='头像'),
        ),
    ]