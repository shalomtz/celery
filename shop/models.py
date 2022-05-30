from email.mime import image
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)


class Shop(models.Model):
    name = models.CharField(max_length=1000)


class Product(models.Model):
    name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)


class Image(models.Model):
    position = models.SmallIntegerField()
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    src = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    pass


class Variant(models.Model):
    pass


class Option(models.Model):
    pass
