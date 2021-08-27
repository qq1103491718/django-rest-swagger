# Generated by Django 2.2.4 on 2021-08-24 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='addr',
            field=models.CharField(default='北京', max_length=20, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='test',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='money',
            field=models.FloatField(default=0, null=True, verbose_name='金额'),
        ),
        migrations.AddField(
            model_name='test',
            name='phone',
            field=models.CharField(default=10086, max_length=11, unique=True, verbose_name='手机号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='test',
            name='work_addr',
            field=models.CharField(default='北京', max_length=20, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=10, verbose_name='名称'),
        ),
    ]