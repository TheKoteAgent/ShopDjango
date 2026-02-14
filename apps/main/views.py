from http.client import HTTPResponse
from .models import Lot, Category
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from apps.reviews.forms import ReviewsForm

def lot_list(request, category_slug=None):
    categories = Category.objects.all()
    lots = Lot.objects.all()

    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        lots = Lot.objects.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        lots = lots.filter(
            Q(title__icontains=search_query) |
            Q(desc__icontains=search_query)
        )

    sort = request.GET.get('sort')
    if sort == 'new':
        lots = lots.order_by('-created_at')
    elif sort == 'old':
        lots = lots.order_by('created_at')
    elif sort == 'popular':
        lots = lots.order_by('views')
    elif sort == 'price_low':
        lots = lots.order_by('price')
    elif sort == 'price_high':
        lots = lots.order_by("-price")
    elif sort == 'name':
        lots = lots.order_by("name")

    paginator = Paginator(lots,1)
    page = request.GET.get('page')

    try:
        lots = paginator.page(page)
    except PageNotAnInteger:
        lots = paginator.page(1)
    except EmptyPage:
        lots = paginator.page(paginator.num_pages)

    return render(request, "main/product_list.html", {
        "title": "Home",
        "lots": lots,
        "categories": categories,
        "category": category,
        "search_query": search_query,
    })

def lot_detail(request, lot_id):
    lot = get_object_or_404(Lot, id=lot_id)
    reviews = lot.reviews.all().order_by('-created_at')
    review_form = ReviewsForm()
    return render(request, "main/product_detail.html", {
        "lot": lot,
        'reviews': reviews,
        'review_form': review_form,
    })