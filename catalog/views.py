from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Catalog
from .table import catalogtable


# Create your views here.
def index(request):
    context = {'title': 'Warehouse'}
    return render(request, 'catalog/index.html', context)

def catalog(request):
    context = {'title': 'Warehouse'}
    """return render(request, 'catalog/catalog.html', {'catalog': catalog.objects.all()})"""
    table = catalogtable(Catalog.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'catalog/catalog.html', {'table': table}, context)
