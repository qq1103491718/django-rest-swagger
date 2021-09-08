
from .serializer import UserSerializer
from rest_framework import viewsets
from .models import UserProfile
from rest_framework.decorators import action, permission_classes, renderer_classes
from rest_framework.response import Response
from utils.pagination import CustomPagination
from utils.pyjwt import jwtencode
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny


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

    # @permission_classes(AllowAny)
    @action(methods=['POST'], detail=False)
    def Login(self, request):
        '''
        登陆用户

        ---
        parameters:
        - name: username
          description: Foobar long description goes here
          required: true
          type: string
        - name: password
          required: true
        '''
        # request.data返回请求正文的解析内容
        user = request.data.get('username')

        pwd = request.data.get('password')
        queryset = UserProfile.objects.filter(
            username=user, password=pwd)

        # 对分页数据进行序列化
        ser = UserSerializer(instance=queryset, many=True)
        if len(ser.data) > 0:
            user = ser.data[0]

            token = jwtencode()
            token.username = user.get('username')
            token.id = user.get('id')
            user['token'] = token.encode()
            return Response(user)
        return Response(data='当前用户名或密码错误！', status=status.HTTP_403_FORBIDDEN)
        # token = Token.objects.create(user=request.user)
        # print(token.key)
        # ser = UserSerializer(instance=user_object, many=True)
        # return Response({'data': '1111'})
