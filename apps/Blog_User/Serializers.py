# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午10:55
# @Author  : void bug
# @FileName: Serializers.py
# @Software: PyCharm
from rest_framework import serializers
from .models import *

class UserSerializers_all:
    class UserSerializers(serializers.ModelSerializer):
        class Meta:
            model = UserModels
            fields = '__all__'
