from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions,authentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
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

class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        existing_user = User.objects.filter(email=data['email']).first()
        if existing_user:
            return Response({'message': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)