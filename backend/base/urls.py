from django.urls import path 
from . import views
from base.api_views import ProductListAPIView,ProductDetailAPIView,GetUserProfileAPIView,UpdateUserProfile,RegisterUserAPIView,LoginAPIView


urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('users/profile/', GetUserProfileAPIView.as_view(), name='users-profiles'),
    path('user/profile/update/', UpdateUserProfile.as_view(), name='users-profile-update'),
    path('user/register/', RegisterUserAPIView.as_view(), name='user-register'),
    path('user/login/', LoginAPIView.as_view(), name='user-login'),
]