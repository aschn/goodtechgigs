from rest_framework import viewsets, serializers
from tags.models import SkillTag, CauseTag

# serializers
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CauseTag


# viewsets
class SkillViewSet(viewsets.ModelViewSet):
    queryset = SkillTag.objects.all()
    serializer_class = SkillSerializer

class CauseViewSet(viewsets.ModelViewSet):
    queryset = CauseTag.objects.all()
    serializer_class = CauseSerializer
