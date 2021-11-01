from django.db import models

# Create your models here.


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    virtual_money = models.FloatField(
        max_length=100, verbose_name='虚拟金额', default=0)
    own_money = models.FloatField(
        max_length=100, verbose_name='实际金额', default=0)
    virtual_borrow_money = models.FloatField(
        max_length=100, verbose_name='虚拟借款金额', default=0)
    borrow_money = models.FloatField(
        max_length=100, verbose_name='实际借款金额', default=0)

    class Meta:
        db_table = 'account'  # 通过db_table自定义数据表名
        ordering = ('-id',)
