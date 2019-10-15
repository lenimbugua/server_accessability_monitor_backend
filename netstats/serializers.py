from rest_framework import serializers
from .models import Stats, FilePath


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'


class FilePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilePath
        fields = '__all__'
