# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午10:55
# @Author  : void bug
# @FileName: Serializers.py
# @Software: PyCharm
from rest_framework import serializers

from apps.Blog.models import *
from apps.Blog_User.Serializers import UserSerializers_all


class CategorySerializers(serializers.ModelSerializer):
    author = UserSerializers_all.Srlist()

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    author = UserSerializers_all.Srlist()

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializers(serializers.ModelSerializer):
    author = UserSerializers_all.Srlist()
    category = CategorySerializers()
    tags = TagSerializers(many=True)

    class Meta:
        model = Article
        fields = '__all__'
