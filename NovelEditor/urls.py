from django.urls import path
from . import views
from rest_framework import routers
from .views import NovelViewSet

app_name = 'NovelHub'


router = routers.DefaultRouter()
router.register(r'novel', NovelViewSet)
