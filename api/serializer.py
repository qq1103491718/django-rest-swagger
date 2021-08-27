# 序列化
from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from api.models import Test
from api.models import Test


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Test
        fields = ['id', 'name', 'addr', 'money', 'phone', 'work_addr']
        # fields = "__all__"
