import os
from django.contrib.gis.utils import LayerMapping
from .models import Railways

railway_mapping = {
    'objectid': 'OBJECTID',
    'fcsubtype': 'FCsubtype',
    'namn1': 'NAMN1',
    'point': 'POINT',
}

railway_geojson = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'RAILWAYS.geojson'),
)

def run(verbose=True):
    lm = LayerMapping(
        Railways, railway_geojson, railway_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)