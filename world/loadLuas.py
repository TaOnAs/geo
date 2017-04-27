import os
from django.contrib.gis.utils import LayerMapping
from .models import LuasStops

luas_mapping = {
    'name': 'Name',
    'point': 'POINT',
}

luasStops = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'luas-stops.geojson'),
)

def run(verbose=True):
    lm = LayerMapping(
        LuasStops, luasStops, luas_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)