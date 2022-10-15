from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image_link = models.URLField(null=True)
    product_name = models.CharField(max_length=100, default="")
    price = models.IntegerField(null=True)
    seller = models.CharField(max_length=100, default="")


class Customer(models.Model):
    phone_number = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=True)
    email_address = models.CharField(max_length=100, null=False)


class AutoBuy(models.Model):
    MONTHLY = 'MTY'
    WEEKLY = 'WKY'
    DAILY = 'DLY'
    REMINDER_CHOICES = [
        (MONTHLY, 'Monthly'),
        (WEEKLY, 'Weekly'),
        (DAILY, 'Daily')
    ]

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    reminder_cycle = models.CharField(max_length = 3, choices=REMINDER_CHOICES, default=DAILY)
    is_autobuy = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['customer', 'product'],
                name = 'unique_customer_product_combo'
            )
        ]
