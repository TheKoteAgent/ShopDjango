from http.client import HTTPResponse
from .models import Lot, Category
from django.shortcuts import render, get_object_or_404

def lot_list(request, category_slug=None):
    categories = Category.objects.all()
    lots = Lot.objects.all()

    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        lots = Lot.objects.filter(category=category)

    sort = request.GET.get('sort')
    if sort == 'new':
        lots = lots.order_by('-created_at')
    elif sort == 'old':
        lots = lots.order_by('created_at')
    elif sort == 'popular':
        lots = lots.order_by('views')
    elif sort == 'price_low':
        lots = lots.order_by('-price')
    elif sort == 'price_high':
        lots = lots.order_by("price")
    elif sort == 'name':
        lots = lots.order_by("name")


    return render(request, "main/product_list.html", {
        "title": "Home",
        "lots": lots,
        "categories": categories,
        "category": category
    })

