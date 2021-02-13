from django.db import models

from apps.Base_app.models import BaseModels
from apps.Blog.models import LinkShowType, Article
from apps.Blog_User.models import UserModels


class Links(BaseModels):
    """广告模块(友情链接)"""
    name = models.CharField('链接名称', max_length=30, unique=True)
    link = models.URLField('链接地址')
    avatar = models.ImageField('显示图片', null=True, upload_to='Links_Img', blank=True)
    sequence = models.IntegerField('排序', unique=True)
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)
    show_type = models.CharField('显示类型', max_length=1, choices=LinkShowType.choices, default=LinkShowType.I)

    class Meta:
        ordering = ['sequence']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class InStationMessages(BaseModels):
    """站内消息通知"""
    name = models.CharField("标题", max_length=100)
    title = models.TextField("内容", max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.title[30]}"

    class Meta:
        db_table = "InStationMessages"
        verbose_name = "站内消息"
        verbose_name_plural = verbose_name


class Message(BaseModels):
    """评论"""
    Article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, verbose_name="文章关联信息")
    user = models.ForeignKey(UserModels, on_delete=models.DO_NOTHING, verbose_name="用户关联信息")
    name = models.CharField("内容", max_length=100)
    to_users = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, verbose_name='回复评论', help_text="回复评论")
    views = models.PositiveIntegerField('点赞数', default=0)
    safe = models.BooleanField("状态(已读/未读)", default=False)

    class Meta:
        db_table = "Message"
        verbose_name = "消息评论"
        verbose_name_plural = verbose_name
        ordering = ['-views', '-create_time', '-update_time']
