
import jwt
import datetime
from jwt import exceptions

from rest_framework.authentication import BaseAuthentication


class jwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("token")
        pa = jwtencode()
        token
        if not token:
            return None
        try:
            pa.decode(encoded=token)
        except exceptions:
            raise exceptions
        # raise

    # def authenticate_header(self, request):
    #     request
    #     """
    #         Return a string to be used as the value of the `WWW-Authenticate`
    #         header in a `401 Unauthenticated` response, or `None` if the
    #         authentication scheme should return `403 Permission Denied` responses.
    #         """
    #     pass


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
        return jwt.decode(encoded, self.key, algorithms=["RS256"])
