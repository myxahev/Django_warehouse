from django.shortcuts import render

# Create your views here.

from django.shortcuts import render




# Create your views here.
def index(request):
    context = {'title': 'Warehouse'}
    return render(request, 'catalog/index.html', context)

def catalog(request):
    context = {'title': 'Warehouse'}
    return render(request, 'catalog/catalog.html', context)

