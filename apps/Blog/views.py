from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from apps.Base_app.Pagination import BasePagination
from .Serializers import *


class CategoryViewSet(ModelViewSet, CacheResponseMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "author": ["exact"],
        "name": ["icontains", "iexact"],
        "language": ["iexact"]
    }


class TagViewSet(ModelViewSet, CacheResponseMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "name": ["icontains", "iexact"],
        "author": ["exact"],
    }


class ArticleViewSet(ModelViewSet, CacheResponseMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        "title": ["icontains", "iexact"],
        "body": ["icontains", "iexact"],
        "author": ["exact"],
        "category": ["exact"],
        "tags": ['exact'],
        "status": ["exact"]
    }
