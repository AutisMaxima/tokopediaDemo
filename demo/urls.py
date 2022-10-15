from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('customers/', CustomerList.as_view()),
    path('customers/<int:pk>', CustomerDetail.as_view()),
    path('autobuy', AutoBuyList.as_view()),
]