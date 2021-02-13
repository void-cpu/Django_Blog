# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午10:55
# @Author  : void bug
# @FileName: Serializers.py
# @Software: PyCharm
from rest_framework import serializers

from .models import *
from ..Blog_User.Serializers import UserSerializers_all


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


class UserMessages_Set_Get_List(serializers.ModelSerializer):
    """此序列化器是默认的序列化器"""
    class Meta:
        model = UserMessages_Set_Get
        fields = '__all__'


class UserMessages_Set_Get_UpDate(serializers.ModelSerializer):
    """此序列化器是进行修改已读和未读状态的序列化器"""
    user = UserSerializers_all.UserReadOnly(read_only=True)
    name = serializers.ReadOnlyField(read_only=True)
    title = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = UserMessages_Set_Get
        fields = '__all__'
