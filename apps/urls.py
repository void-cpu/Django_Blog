# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午11:00
# @Author  : void bug
# @FileName: urls.py
# @Software: PyCharm
from rest_framework.routers import DefaultRouter

from apps.Blog_User.views import (UserViewSet)

routers = DefaultRouter()
routers.register('User', UserViewSet, basename="角色信息管理")
