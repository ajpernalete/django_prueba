from django.urls import path

from . import views


urlpatterns = [
    path('<slug:slug>', views.ProductDetailList.as_view(), name='product') #id -> llave primaria o primary key
]