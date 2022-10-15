from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField(null=True)


class Customer(models.Model):
    phone_number = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=True)
    email_address = models.CharField(max_length=100, null=False)
