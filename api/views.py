# 视图
from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets
from api.serializer import GroupSerializer, TestSerializer, PermissionSerializer
# Create your views here.
from api.models import Test
from rest_framework.response import Response
from rest_framework.decorators import action, renderer_classes
from utils.pagination import CustomPagination
from utils.rendererresponse import customrenderer


# class UserViewSet(viewsets.ModelViewSet):
#     '''查看，编辑用户的界面'''
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''查看，编辑组的界面'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    '''查看，编辑组的界面'''
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class TestViewSet(viewsets.ModelViewSet):
    '''crud 接口'''

    @action(methods=['POST'], detail=False)
    def getListTest(self, request):
        """获取所有test的数据"""
        queryset = Test.objects.all()
        # 创建分页对象
        pg = CustomPagination()
        # 在数据库中获取分页数据
        pager_roles = pg.paginate_queryset(
            queryset=queryset, request=request, view=self)
        # 对分页数据进行序列化
        ser = TestSerializer(instance=pager_roles, many=True)
        return pg.get_paginated_response(ser.data)

    queryset = Test.objects.all()
    serializer_class = TestSerializer
    renderer_classes = [customrenderer]
    pagination_class = CustomPagination
    # authentication_classes=[SessionAuthentication, BasicAuthentication]
