from .products import products
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions,authentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
# Create your views here.
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = '_id'
    
class GetUserProfileAPIView(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)