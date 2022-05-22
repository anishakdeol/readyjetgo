from rest_framework import serializers
from travel.models import Travel

# Travel Serializer
class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'
