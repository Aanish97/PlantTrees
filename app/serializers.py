from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import Plant


class PlantsSerializer(ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Plant
        fields = ('user', 'area', 'description', 'file', 'stars', 'created_at', )
