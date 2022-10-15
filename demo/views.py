from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def index(request):
    return HttpResponse('Hello World!')
