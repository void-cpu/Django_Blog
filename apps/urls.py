# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 下午11:00
# @Author  : void bug
# @FileName: urls.py
# @Software: PyCharm
from rest_framework.routers import DefaultRouter

from apps.Blog.views import CategoryViewSet, TagViewSet, ArticleViewSet
from apps.BlogAnother.views import Links_yViewSet, InStationMessages_yViewSet, Messages_yViewSet, \
    UserMessage_Set_Get_ViewSet
from apps.Blog_User.views import (UserViewSet)

routers = DefaultRouter()
routers.register('User', UserViewSet, basename="用户信息管理")
routers.register('Cate', CategoryViewSet, basename="分类信息管理")
routers.register("Tag", TagViewSet, basename="标签信息管理")
routers.register("Article", ArticleViewSet, basename="文章信息管理")
routers.register("Links", Links_yViewSet, basename="广告信息管理")
routers.register("InStationMessages", InStationMessages_yViewSet, basename="站内消息信息管理")
routers.register('Messages', Messages_yViewSet, basename="评论消息信息管理")
routers.register("UserMessages", UserMessage_Set_Get_ViewSet, basename="用户收件箱信息管理")
