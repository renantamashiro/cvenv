from rest_framework import viewsets

from .models.logs import Group, Level, Log
from .serializers import (
    GroupModelSerializer,
    LevelModelSerializer,
    LogModelSerializer
)


class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogModelSerializer


# Create your views here
