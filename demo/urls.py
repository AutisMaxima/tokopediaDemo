from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view())
]