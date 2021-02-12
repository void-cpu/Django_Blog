from django.contrib import admin

from apps.Blog.models import Category, Tag, Article

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
