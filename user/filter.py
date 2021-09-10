# filters.py
import django_filters

from .models import UserProfile


class userFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name='username', lookup_expr='contains')
    start_date = django_filters.DateFilter(
        field_name='birthday', lookup_expr=('gt'),)
    end_date = django_filters.DateFilter(
        field_name='birthday', lookup_expr=('lt'))

    class Meta:
        model = UserProfile  # 模型名
        fields = ['username', 'birthday']
