"""apitest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from api import views
from user.views import *
# from rest_framework_simplejwt.views import (TokenObtainPariView)
# 路由
router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet, base_name='组')
router.register(r'user', UserViewSet, base_name='用户')
router.register(r'test', views.TestViewSet, base_name='测试')
router.register(r'permission', views.PermissionViewSet, base_name='权限组')
# router.register(r'token', JSONWebTokenAPIView, base_name='token')
# 重要的是如下三行
schema_view = get_schema_view(title='Users API', renderer_classes=[
                              OpenAPIRenderer, SwaggerUIRenderer])
urlpatterns = [
    # swagger接口文档路由
    url(r'^docs/', schema_view, name="docs"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # drf登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # rest_framework_simplejwt自带的得到token
    path('user/token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # 刷新JWT
    path('user/v1/token/refresh/',
         MyTokenRefreshView.as_view(), name='token_refresh'),
]
