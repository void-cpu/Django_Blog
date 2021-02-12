from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .Serializers import *


class UserViewSet(ModelViewSet):
    """
    角色信息管理
    """
    queryset = UserModels.objects.all()
    serializer_class = UserSerializers_all.UserSerializers

