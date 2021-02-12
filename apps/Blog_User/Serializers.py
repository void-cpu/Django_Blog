# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午10:55
# @Author  : void bug
# @FileName: Serializers.py
# @Software: PyCharm
from rest_framework import serializers
from .models import *


class UserSerializers_all:
    class Srlist(serializers.ModelSerializer):
        class Meta:
            model = UserModels
            fields = '__all__'

    class UserCreate(serializers.ModelSerializer):
        phone = serializers.ReadOnlyField(read_only=True)
        avatar = serializers.FileField(read_only=True)

        class Meta:
            model = UserModels
            fields = '__all__'

    class UserUpdate(serializers.ModelSerializer):
        pass_word = serializers.ReadOnlyField(read_only=True)

        class Meta:
            model = UserModels
            fields = '__all__'

    class UserReadOnly(serializers.ModelSerializer):
        user_name = pass_word = phone = serializers.ReadOnlyField(read_only=True)
        avatar = serializers.FileField(read_only=True)

        class Meta:
            model = UserModels
            fields = '__all__'
