
from .serializer import UserSerializer
from rest_framework import viewsets
from .models import UserProfile
from rest_framework.decorators import action, renderer_classes
from rest_framework.response import Response
from utils.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import *
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from .serializer import *
from .models import *


class UserViewSet(
        viewsets.ModelViewSet):
    '''
                retrieve:
                    获取用户信息

                list:
                    获取所有用户信息

                create:
                    创建用户

                delete:
                    删除用户

                partial_update:
                    更改一个或多个用户

                update:
                    更改一个用户
            '''
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=False)
    def Login(self, request):
        '''
        登陆用户
        ---
        parameters:
        - name: some_param
          description: Foobar long description goes here
          required: true
          type: integer
          paramType: form
        - name: other_foo
          paramType: query
        - name: avatar
          type: file
        '''
        # request.data返回请求正文的解析内容
        user = request.data.get('username')

        pwd = request.data.get('password')
        queryset = UserProfile.objects.filter(
            username=user, password=pwd)
        pg = CustomPagination()
        # 在数据库中获取分页数据
        pager_roles = pg.paginate_queryset(
            queryset=queryset, request=request, view=self)
        # 对分页数据进行序列化
        ser = UserSerializer(instance=pager_roles, many=True)
        # token = Token.objects.create(user=request.user)
        # print(token.key)
        return Response(ser.data)
        # ser = UserSerializer(instance=user_object, many=True)
        # return Response({'data': '1111'})


class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义得到token username: 账号或者密码 password: 密码或者验证码
    """
    www_authenticate_realm = 'user'
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """
    www_authenticate_realm = 'user'
    serializer_class = TokenRefreshSerializer
