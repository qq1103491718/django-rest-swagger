
import jwt
import datetime
from rest_framework.authentication import BaseAuthentication
from rest_framework.views import exception_handler


class jwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_TOKEN")
        pa = jwtencode()
        token
        if not token:
            return None


class jwtencode:

    # 密钥
    key = 'jwoofnasdkoasgfk'
    # 用户名
    username = None
    # 用户id
    id = None
    # 过期时间
    expday = 1
    # 加密算法
    algorithm = 'HS256'

    def encode(self):
        dic = {
            'exp': datetime.datetime.now() + datetime.timedelta(days=self.expday),  # 过期时间
            'iat': datetime.datetime.now(),  # 开始时间
            'iss': 'lianzong',  # 签名
            'data': {  # 内容，一般存放该用户id和开始时间
                'username': self.username,
                'id': self.id,
            },
        }
        return jwt.encode(dic, self.key, algorithm=self.algorithm)

    def decode(self, encoded=None):
        if encoded:
            try:
                user = jwt.decode(encoded, self.key, algorithms=['HS256'])
                return True
            except:
                return False
        return False
        # print(jwt.decode(encoded, self.key, algorithms=['HS256']))
