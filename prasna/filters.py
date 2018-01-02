from django_filters import rest_framework as filters

from prasna.models import QuizItem


class QuizItemFilter(filters.FilterSet):
    a_text__icontains = filters.CharFilter(name='a_text', lookup_expr='icontains')
    q_text__icontains = filters.CharFilter(name='q_text', lookup_expr='icontains')
    category = filters.ModelChoiceFilter(choices=QuizItem.LEVELS)
    difficulty = filters.CharFilter(lookup_expr='iexact')
    age = filters.NumericRangeFilter(name='age')
