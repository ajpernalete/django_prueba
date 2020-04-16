from django.urls import path

from . import views


urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailList.as_view(), name='product'), #id -> llave primaria o primary key

]