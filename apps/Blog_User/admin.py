from django.contrib import admin

from apps.Blog_User.models import *


@admin.register(UserModels)
class UserAdmin(admin.ModelAdmin):
    pass
