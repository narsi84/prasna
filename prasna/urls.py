from django.conf.urls import include
from django.urls import path

from django.contrib import admin
from rest_framework import routers

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from prasna.views import QuizItemViewSet, CategoryViewSet, QuestionViewSet

schema_view = get_swagger_view(title='Quiz API')

admin.autodiscover()

router = routers.DefaultRouter()
router.register('quiz-items', QuizItemViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'api/docs/', schema_view),
    path('<mode>', QuestionViewSet.as_view())
]