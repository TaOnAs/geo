from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# class WorldBorder(models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()
#
#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = models.MultiPolygonField()
#
#     # Returns the string representation of the model.
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class User(AbstractUser):
#     last_location = models.PointField(
#         verbose_name="last known location",
#         blank=True,
#         null=True
#     )
#     created = models.DateTimeField(
#         auto_now_add=True
#     )
#     modified = models.DateTimeField(
#         auto_now=True
#     )
#
#     # objects = models.GeoManager()
#
#     def __str__(self):
#         return "{}, ({}), last seen at {} ... cr={}, mod={}" \
#             .format(self.username, self.get_full_name(), self.last_location, self.created, self.modified)


class Railways(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # Railways.geojson
    objectid = models.IntegerField()
    fcsubtype = models.IntegerField()
    namn1 = models.CharField(max_length=100)
    point = models.PointField(
        blank=True,
        null=True
    )


    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.namn1

class LuasStops(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # Railways.geojson
    name = models.CharField(max_length=100)
    point = models.PointField(
        blank=True,
        null=True
    )


    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)