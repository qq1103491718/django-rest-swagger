# 视图

from rest_framework import viewsets
from api.serializer import TestSerializer
# Create your views here.
from api.models import Test


class TestViewSet(viewsets.ModelViewSet):
    '''Test增删改查的界面'''
    queryset = Test.objects.all()
    serializer_class = TestSerializer
