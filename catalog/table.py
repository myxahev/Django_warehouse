import django_tables2 as tables
from .models import Catalog

class catalogtable(tables.Table):
    class Meta:
        model = Catalog
        template_name = "django_tables2/bootstrap.html"
        #attrs = {'class': 'paleblue'}



