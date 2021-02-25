from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .Serializers import *
from ..Base_app.Pagination import BasePagination


class Links_yViewSet(ReadOnlyModelViewSet, CacheResponseMixin):
    queryset = Links.objects.all()
    serializer_class = LinksSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "name": ["icontains", "iexact"],
        "is_enable": ["exact"],
        "show_type": ['exact']
    }


class InStationMessages_yViewSet(ReadOnlyModelViewSet, CacheResponseMixin):
    queryset = InStationMessages.objects.all()
    serializer_class = InStationMessagesSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "name": ["icontains", "iexact"],
        "title": ["icontains", "iexact"],
    }


class Messages_yViewSet(ModelViewSet, CacheResponseMixin):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "Article": ["exact"],
        'user': ["exact"],
        'safe': ["exact"],
        'name': ["icontains", "iexact"],
        "to_users": ["exact"],
    }


class UserMessage_Set_Get_ViewSet(ModelViewSet):
    queryset = UserMessages_Set_Get.objects.all()
    serializer_class = UserMessages_Set_Get_List
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "user": ["exact"],
        "name": ["icontains", "iexact"],
        "title": ["icontains", "iexact"],
        "Safe": ["exact"]
    }

    def get_serializer_class(self):
        if self.action == "update":
            return UserMessages_Set_Get_UpDate
        else:
            return UserMessages_Set_Get_List
