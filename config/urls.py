from django.contrib import admin
from django.urls import path, include
from NovelEditor.urls import router as novel_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(novel_router.urls)),
]
