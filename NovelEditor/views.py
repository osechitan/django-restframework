from .models import Novel
from rest_framework import viewsets
from .serializer import NovelSerializer


class NovelViewSet(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
