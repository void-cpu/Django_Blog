# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午11:00
# @Author  : void bug
# @FileName: urls.py
# @Software: PyCharm
from rest_framework.routers import DefaultRouter

from apps.Blog.views import CategoryViewSet, TagViewSet, ArticleViewSet
from apps.Blog_User.views import (UserViewSet)

routers = DefaultRouter()
routers.register('User', UserViewSet, basename="用户信息管理")
routers.register('Tag', CategoryViewSet, basename="分类信息管理")
routers.register("Tag", TagViewSet, basename="标签信息管理")
routers.register("Article", ArticleViewSet, basename="文章信息管理")
