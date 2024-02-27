from django.db import models


class Order(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    pass


class Staff(models.Model):
    full_name = models.CharField(max_length=255)  # ...CharField(max_length=255, null = True)
    position = models.CharField(max_length=255)
    labor_contract = models.IntegerField()


class ProductOrder(models.Model):
    pass
