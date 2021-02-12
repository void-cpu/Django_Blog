from django.db import models
from pygments.lexers import get_all_lexers

from apps.Base_app.models import BaseModels
from apps.Blog_User.models import UserModels

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Category(BaseModels):
    name = models.CharField("分类名", max_length=30)
    avatar = models.ImageField('显示图片', null=True, upload_to='Category_img', blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    author = models.ForeignKey(UserModels, verbose_name='持有人', blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-create_time', '-update_time']
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(BaseModels):
    name = models.CharField("分类名", max_length=30)
    avatar = models.ImageField('显示图片', null=True, upload_to='Category_img', blank=True)
    author = models.ForeignKey(UserModels, verbose_name='持有人', blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-create_time', '-update_time']
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(BaseModels):
    """文章"""
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    COMMENT_STATUS = (
        ('o', '打开'),
        ('c', '关闭'),
    )
    TYPE = (
        ('a', '文章'),
        ('p', '页面'),
    )
    title = models.CharField('标题', max_length=200, unique=True)
    body = models.TextField('正文')
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    comment_status = models.CharField('评论状态', max_length=1, choices=COMMENT_STATUS, default='o')
    type = models.CharField('类型', max_length=1, choices=TYPE, default='a')
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(UserModels, verbose_name='作者', blank=False, null=False, on_delete=models.CASCADE)
    article_order = models.IntegerField('排序,数字越大越靠前', blank=False, null=False, default=0)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time', '-update_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
