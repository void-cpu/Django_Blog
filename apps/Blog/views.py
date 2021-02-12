from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from apps.Base_app.Pagination import BasePagination
from .Serializers import *

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("author", "name", "language")

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("name", "author")

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("title", "status", 'author', 'category', 'tags')
