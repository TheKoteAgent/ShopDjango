from django.contrib import admin
from .models import Lot
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_editable = ("title",)

@admin.register(Lot)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title", "desc", "price")
    list_editable = ("category", "title", "desc", "price")
    search_fields = ("id", "title")
    list_filter = ("is_available", "created_at", "price")
