from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        input_name = self.request.query_params.get('name')
        if input_name is not None:
            queryset = queryset.filter(name=input_name)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


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


def index(request):
    return HttpResponse('Hello World!')
