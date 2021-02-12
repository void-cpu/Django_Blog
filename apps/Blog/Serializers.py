# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午10:55
# @Author  : void bug
# @FileName: Serializers.py
# @Software: PyCharm
from rest_framework import serializers

from apps.Blog.models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
