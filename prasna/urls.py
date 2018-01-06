from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path

from django.contrib import admin
from rest_framework import routers

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from prasna.views import QuizItemViewSet, CategoryViewSet, QuestionViewSet, MediaViewSet

schema_view = get_swagger_view(title='Quiz API')

admin.autodiscover()

router = routers.DefaultRouter()
router.register('quiz-items', QuizItemViewSet)
router.register('categories', CategoryViewSet)
router.register('media', MediaViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'api/docs/', schema_view),
    path('<mode>', QuestionViewSet.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)