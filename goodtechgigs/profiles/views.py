from rest_framework import viewsets, serializers
from profiles.models import GigPoster, GigSeeker

# serializers
class GigPosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GigPoster

class GigSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GigSeeker


# viewsets
class GigPosterViewSet(viewsets.ModelViewSet):
    queryset = GigPoster.objects.all()
    serializer_class = GigPosterSerializer

class GigSeekerViewSet(viewsets.ModelViewSet):
    queryset = GigSeeker.objects.all()
    serializer_class = GigSeekerSerializer
