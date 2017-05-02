from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from world import models
from world import serializers
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class RailwaysView(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated)
    def get_queryset(self):
        return models.Railways.objects
    model = models.Railways
    serializer_class = serializers.RailwaysSerializer


class LuasView(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated)
    def get_queryset(self):
        return models.LuasStops.objects
    model = models.LuasStops
    serializer_class = serializers.LuasSerializer

class LuasPointView(generics.ListAPIView):

    def get_queryset(self):
        lat = self.request.GET.get('lat')
        lng = self.request.GET.get('lng')
        pnt = Point(float(lat), float(lng))
        return models.LuasStops.objects.filter(point=pnt)

    model = models.LuasStops
    serializer_class = serializers.LuasSerializer