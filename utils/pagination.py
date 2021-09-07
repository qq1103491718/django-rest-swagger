# 分页器
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'page_size': self.page_size,
            'counts': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'data': data
        })
