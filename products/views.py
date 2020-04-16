from django.shortcuts import render

from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos '
        return context

class ProductDetailList(DetailView): #id -> pk
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class ProductSearchListView(ListView):
    template_name='products/search.html'
    
    
    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(categories__title__icontains=self.query())

        #SELECT * FROM products WHERE title like %valor%
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        return context

