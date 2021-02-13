from django.contrib import admin

from apps.BlogAnother.models import *

admin.site.register(Links)

admin.site.register(Message)


@admin.register(UserMessages_Set_Get)
class UserMessages_Set_GetAdmin(admin.ModelAdmin):
    pass


@admin.register(InStationMessages)
class InStationMessagesAdmin(admin.ModelAdmin):
    actions = ['add_UserMessages_Set_Get_Admin']

    def add_UserMessages_Set_Get_Admin(self, request, queryset):
        for _object in queryset.filter():
            for i in UserModels.objects.all():
                UserMessages_Set_Get.objects.create(user=i, name=_object.name, title=_object.title)

    add_UserMessages_Set_Get_Admin.short_description = "发送信息"
