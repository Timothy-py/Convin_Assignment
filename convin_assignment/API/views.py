from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import MultiPartParser, FormParser

from . import serializers
from system1.models import File


class FileUpdateView(generics.UpdateAPIView, UpdateModelMixin):
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'id'