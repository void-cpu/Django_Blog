# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午10:55
# @Author  : void bug
# @FileName: Serializers.py
# @Software: PyCharm
from rest_framework import serializers

from .models import *


class LinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'


class InStationMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = InStationMessages
        fields = '__all__'


class MessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
