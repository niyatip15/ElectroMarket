from django.urls import path 
from . import views
from base.views import *
urlpatterns = [
    path('products/',views.getProducts, name='get-products'),
    path('products/<int:id>/',views.getProduct, name='get-product')
    
    
]