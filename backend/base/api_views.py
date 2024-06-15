from .products import products
from rest_framework.generics import ListAPIView,RetrieveAPIView
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