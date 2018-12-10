from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from decimal import *
from .models import *
from math import sin, cos, sqrt, atan2, radians
from django.db import connection

class Interviewapi1(APIView):
    serializer_class = serializers.LocSerializer

    def post(self, request):

        serializer = serializers.LocSerializer(data=request.data)
        z=Location.objects.all()
        if serializer.is_valid():
            pincode = serializer.validated_data.get('pincode')
            lat = serializer.validated_data.get('lat')
            lng = serializer.validated_data.get('lng')
            c=0
            for i in z:
                if i.lat is not None and i.lng is not None:
                    i.lat=Decimal(i.lat)
                    i.lng=Decimal(i.lng)
                else:
                    i.lat,i.lng=0,0
                    i.lat=Decimal(i.lat)
                    i.lng=Decimal(i.lng)
                if i.pincode == pincode or (i.lat >= (Decimal(lat)-Decimal(0.1000)) and i.lat <= (Decimal(lat)+Decimal(0.1000)) and i.lng >= (Decimal(lng)-Decimal(0.1000)) and i.lng <= (Decimal(lng)+Decimal(0.1000))):
                     c=1
            if c==0:
                user_obj =Location.objects.create(pincode=request.POST.get('pincode'),address=request.POST.get('address'),city=request.POST.get('city'),lat=request.POST.get('lat'),lng=request.POST.get('lng'))
                user_obj.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'data already exists'})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Interviewapi2(APIView):
    serializer_class = serializers.RadSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello! Please enter the location and radius below'})

    def post(self, request):

        serializer = serializers.RadSerializer(data=request.data)
        z=Location.objects.all()
        if serializer.is_valid():
            lat = serializer.validated_data.get('lat')
            lng = serializer.validated_data.get('lng')
            radius = serializer.validated_data.get('radius')
            radius=radius*1000
            cursor = connection.cursor()
            cursor.execute('SELECT interview1_Location.pincode,interview1_Location.address,interview1_Location.city FROM interview1_Location WHERE earth_box(ll_to_earth(%s,%s), %s) @> ll_to_earth(interview1_Location.lat, interview1_Location.lng)',[lat,lng,radius])
            w=cursor.fetchall()
            return Response({'data':w})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Interviewapi2b(APIView):
    serializer_class = serializers.RadSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello! Please enter the location and radius below'})

    def post(self, request):

        serializer = serializers.RadSerializer(data=request.data)
        z=Location.objects.all()
        if serializer.is_valid():
            lat = serializer.validated_data.get('lat')
            lng = serializer.validated_data.get('lng')
            radius = serializer.validated_data.get('radius')
            s=[]
            for i in z:
                if i.lat is not None and i.lng is not None:
                    i.lat=Decimal(i.lat)
                    i.lng=Decimal(i.lng)
                else:
                    i.lat,i.lng=0,0
                    i.lat=Decimal(i.lat)
                    i.lng=Decimal(i.lng)
                R = 6373.0
                lat1 = radians(lat)
                lon1 = radians(lng)
                lat2 = radians(i.lat)
                lon2 = radians(i.lng)
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distance = R * c
                if distance<=radius:
                    s.append((i.pincode,i.address,i.city))
            return Response({'data': s})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Interviewapi3(APIView):
    serializer_class = serializers.GeoSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello! Please enter the location below'})

    def post(self, request):

        serializer = serializers.GeoSerializer(data=request.data)

        if serializer.is_valid():
            lng = serializer.validated_data.get('lng')
            lat = serializer.validated_data.get('lat')

            cursor = connection.cursor()
            cursor.execute("SELECT geoloc.name FROM geoloc WHERE ST_Contains(geoloc.geom,ST_Transform(ST_GeomFromText('POINT(%s %s)', 4326), 4326))",[lng,lat])
            w=cursor.fetchall()
            return Response({'Place': w})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
