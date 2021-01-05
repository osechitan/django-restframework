from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'NovelEditor'

router = routers.DefaultRouter()
router.register('novel', views.NovelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
