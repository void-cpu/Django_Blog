# Generated by Django 3.1.6 on 2021-02-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='链接名称')),
                ('link', models.URLField(verbose_name='链接地址')),
                ('sequence', models.IntegerField(unique=True, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否显示')),
                ('show_type', models.CharField(choices=[('i', '首页'), ('l', '列表页'), ('p', '文章页面'), ('a', '全站'), ('s', '友情链接页面')], default='i', max_length=1, verbose_name='显示类型')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['sequence'],
            },
        ),
    ]
