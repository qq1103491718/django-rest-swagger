# 视图
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializer import UserSerializer, GroupSerializer, TestSerializer
# Create your views here.
from api.models import Test
from rest_framework.response import Response
from rest_framework.decorators import action, renderer_classes

from utils.rendererresponse import customrenderer


class UserViewSet(viewsets.ModelViewSet):
    '''查看，编辑用户的界面'''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''查看，编辑组的界面'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TestViewSet(viewsets.ModelViewSet):
    '''crud 接口'''

    @action(methods=['POST'], detail=False)
    def getListTest(self, request):
        """获取所有test的数据"""
        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)

    queryset = Test.objects.all()
    serializer_class = TestSerializer
    renderer_classes = [customrenderer]
