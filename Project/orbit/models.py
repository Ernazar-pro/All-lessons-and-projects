from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    date_joined = models.DateField()

class Category(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey('User', related_name='categories', on_delete=models.CASCADE)

class User(models.Model):
    full_name = models.CharField(max_length=15)
