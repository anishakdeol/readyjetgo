from travel.models import Travel
from rest_framework import viewsets, permissions
from .serializers import TravelSerializer

# Travel Viewset
class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    permission_classes = [
        permissions.AllowAny
        ]
    serializer_class = TravelSerializer
