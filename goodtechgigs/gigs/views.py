from rest_framework import viewsets, serializers
from gigs.models import Gig

# serializers
class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig


# viewsets
class GigViewSet(viewsets.ModelViewSet):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
