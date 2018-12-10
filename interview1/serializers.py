from rest_framework import serializers
from .models import *

class LocSerializer(serializers.Serializer):
    pincode=serializers.CharField(max_length=20)
    address=serializers.CharField(max_length=200)
    city=serializers.CharField(max_length=100)
    lat=serializers.DecimalField(max_digits=6, decimal_places=4)
    lng=serializers.DecimalField(max_digits=6, decimal_places=4)

    def create(self, validated_data):
        return Location(**validated_data)

    class Meta:
        model=Location
        fields="__all__"

class RadSerializer(serializers.Serializer):
    lat=serializers.DecimalField(max_digits=6, decimal_places=4)
    lng=serializers.DecimalField(max_digits=6, decimal_places=4)
    radius=serializers.IntegerField()

class GeoSerializer(serializers.Serializer):
    lng=serializers.DecimalField(max_digits=17, decimal_places=15)
    lat=serializers.DecimalField(max_digits=17, decimal_places=15)
