import django_tables2 as tables
from .models import Catalog

class catalogtable(tables.Table):
    class Meta:
        model = Catalog
        attrs = {'class': 'paleblue'}