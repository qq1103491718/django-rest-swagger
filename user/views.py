
from rest_framework.serializers import SerializerMetaclass
from rest_framework.generics import GenericAPIView
from .serializer import UserSerializer, userFilter
from utils.mixins import commonViewsets
from .models import UserProfile
from rest_framework.response import Response
from utils.pagination import CustomPagination
from utils.pyjwt import jwtencode
from utils.authenticated import isMyTokenPermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.filters import SearchFilter
# from .filter import userFilter


class UserViewSet(
        commonViewsets):
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
    permission_classes = [isMyTokenPermission]


class userLoginView(GenericAPIView):
    serializer_class = userFilter

    def post(self, request, *args, **kwargs):
        '''
        登陆用户

        '''

        # request.data返回请求正文的解析内容
        user = request.data.get('username')

        pwd = request.data.get('password')
        queryset = UserProfile.objects.filter(
            username=user, password=pwd)

        # 对分页数据进行序列化
        ser = userFilter(instance=queryset, many=True)
        if len(ser.data) > 0:
            user = ser.data[0]

            token = jwtencode()
            token.username = user.get('username')
            token.id = user.get('id')
            user['token'] = token.encode()
            return Response(user)
        raise AuthenticationFailed
        # return Response(data='当前用户名或密码错误！', status=status.HTTP_403_FORBIDDEN)
