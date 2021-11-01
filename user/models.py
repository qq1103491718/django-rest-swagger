# apps.users.models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from rest_framework.permissions
from account.models import Account


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True,
                            help_text=_('测试用的用户名'),
                            blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True,
                                help_text='测试用的生日',
                                blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6,
                              choices=(
                                  ("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True,
                              max_length=11, verbose_name="电话")
    email = models.EmailField(
        max_length=100, null=True,
        blank=True, verbose_name="邮箱")
    # account = models.ForeignKey(
    #     Account, related_name='account', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
