from rest_framework.serializers import ModelSerializer

from app.models import Plant


class PlantsSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = ('user', 'title', 'description',
                  'file', 'created_at', )
