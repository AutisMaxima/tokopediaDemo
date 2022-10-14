from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

class ItemView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def index(request):
    return HttpResponse('Hello World!')
