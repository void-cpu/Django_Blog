from django.db import models

from apps.Base_app.models import BaseModels


class UserModels(BaseModels):
    user_name = models.CharField("用户名", max_length=20, unique=True)
    pass_word = models.CharField("用户密码", max_length=300)
    phone = models.CharField("电话", max_length=30, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
