from django.urls import path 
from . import views
from base.api_views import *
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    
    
]