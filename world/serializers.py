from world import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import GEOSGeometry, LineString, Point, Polygon


class RailwaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Railways
        fields = ('id', 'objectid', 'fcsubtype', 'namn1', 'point')


class LuasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LuasStops
        fields = ('id', 'name', 'point')

