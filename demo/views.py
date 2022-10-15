from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.
class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        input_name = self.request.query_params.get('product_name')
        if input_name is not None:
            queryset = queryset.filter(name__icontains=input_name)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        input_phone_number = self.request.query_params.get('phonenumber')
        if input_phone_number is not None:
            queryset = queryset.filter(phone_number=input_phone_number)
        return queryset


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AutoBuyList(generics.ListCreateAPIView):
    serializer_class = AutoBuySerializer

    def get_queryset(self):
        queryset = AutoBuy.objects.all()
        input_customer_name = self.request.query_params.get('customername')
        if input_customer_name is not None:
            queryset.filter(customer__full_name=input_customer_name)
        return queryset


class AutoBuyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutoBuy.objects.all()
    serializer_class = AutoBuySerializer


def index(request):
    return HttpResponse('Hello World!')
