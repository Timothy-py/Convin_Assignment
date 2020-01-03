from rest_framework import serializers
from system1.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta():
        model = File
        fields = ('id', 'file_object')