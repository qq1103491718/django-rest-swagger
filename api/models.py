# models.py
from django.db import models


class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=10)
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    money = models.FloatField(verbose_name='金额', default=0, null=True)
    addr = models.CharField(verbose_name='地址', default='北京', max_length=20)
    work_addr = models.CharField(
        verbose_name='地址', default='北京', max_length=20)
    # auto_now_add的意思，插入数据的时候，自动取当前时间
    create_time = models.DateTimeField(
        verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'test'  # 通过db_table自定义数据表名
