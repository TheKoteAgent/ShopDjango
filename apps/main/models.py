from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    desc = models.TextField(max_length=300)
    img = models.ImageField(upload_to="category/", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("main:lot_list", args=[self.slug])

class Lot(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000)
    img = models.ImageField(upload_to="lots/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_available = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("main:lot_list", args=[self.slug])