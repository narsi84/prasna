import random

from psycopg2._range import NumericRange
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from prasna.filters import QuizItemFilter
from prasna.models import QuizItem, Category, Media
from prasna.serializers import CategorySerializer, QuizItemSerializer, MediaSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('name',)


class QuizItemViewSet(ModelViewSet):
    queryset = QuizItem.objects.select_related('category').all()
    serializer_class = QuizItemSerializer
    filter_class = QuizItemFilter


class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class QuestionViewSet(APIView):
    def get(self, request, mode):
        filters = {}
        print(request.query_params)
        if request.query_params.get('categories', ''):
            filters['category__name__in'] = request.query_params['categories'].split(',')

        min_age = int(request.query_params.get('min_age', 0))
        max_age = int(request.query_params.get('max_age', 100))
        filters['age__overlap'] = NumericRange(min_age, max_age)

        if 'levels' in request.query_params:
            filters['difficulty__in'] = [int(x) for x in request.query_params['levels'].split(',')]

        q_items = QuizItem.objects.filter(**filters)

        ids = q_items.values_list('id', flat=True)

        if mode == 'learn':
            rand_id = ids[random.randint(0, len(ids) - 1)]
            q_item = q_items.get(pk=rand_id)
            return Response(QuizItemSerializer(q_item).data)
        else:
            rand_ids = random.sample(list(ids), min(4, len(ids)))
            return Response(
                [QuizItemSerializer(q_item).data for q_item in q_items.filter(pk__in=rand_ids)]
            )
