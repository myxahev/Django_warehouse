from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django_tables2 import RequestConfig, SingleTableView
from .models import Catalog
from .table import catalogtable
#from .forms import LoginForm


# Create your views here.
def index(request):
    context = {'title': 'Warehouse'}
    return render(request, 'catalog/index.html', context)

def catalog(request):
    context = {'title': 'Warehouse'}
    #return render(request, 'catalog/catalog.html', {'catalog': catalog.objects.all()})
    table = catalogtable(Catalog.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'catalog/catalog.html', {'table': table}, context)


#class LoginView(**, View):
#
#    def get(self, request, *args, **kwargs):
#        form = LoginForm(request.POST or None)
#        categories = Category.object.all()
#        context = {'form': form, 'categories': categories, 'card': self.card}
#        return render(request, 'login.html', context)


class CatalogListView(SingleTableView):
    model = Catalog
    table_class = catalogtable
    template_name = 'catalog/catalog.html'