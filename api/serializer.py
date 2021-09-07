# 序列化
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
# from api.models import Test
from api.models import Test
from rest_framework.validators import UniqueValidator
from django.core import validators


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    phone = serializers.CharField(required=True,
                                  validators=[validators.RegexValidator(
                                      r'1[3-9]\d{9}', message='请输入正确手机号码'),
                                      UniqueValidator(queryset=Test.objects.all(), message='手机号码不能重复')],
                                  error_messages={
                                      'blank': '电话不能为空',
                                      'max_length': '超出电话号码最大长度'
                                  }, max_length=11)

    class Meta:
        model = Test
        fields = ['id', 'name', 'addr', 'money', 'phone', 'work_addr']
        # fields = "__all__"
