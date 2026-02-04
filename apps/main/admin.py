from django.contrib import admin
from .models import Lot
from .models import Category
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_editable = ("title",)
    prepopulated_fields = {"slug": ("title",)}

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px" />',
                obj.image.url,
            )
        return format_html('<span>не має зображення</span>')

    image_tag.short_description = "Image"


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title", "desc", "price")
    list_editable = ("category", "title", "desc", "price")
    search_fields = ("id", "title")
    list_filter = ("is_available", "created_at", "price")
    prepopulated_fields = {"slug": ("title",)}
