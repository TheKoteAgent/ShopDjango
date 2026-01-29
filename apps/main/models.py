from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

class Lot(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)