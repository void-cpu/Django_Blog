from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .Serializers import *
from ..Base_app.Pagination import BasePagination


class Links_yViewSet(ReadOnlyModelViewSet, CacheResponseMixin):
    queryset = Links.objects.all()
    serializer_class = LinksSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("name", "is_enable", "show_type")

class InStationMessages_yViewSet(ReadOnlyModelViewSet, CacheResponseMixin):
    queryset = InStationMessages.objects.all()
    serializer_class = InStationMessagesSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("name", )

class Messages_yViewSet(ReadOnlyModelViewSet, CacheResponseMixin):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("Article", 'user', 'safe')
