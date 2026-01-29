from http.client import HTTPResponse
from .models import Lot
from django.shortcuts import render

def lot_list(request):
    lots = Lot.objects.all()
    return render(request, "main/product_list.html", {"title": "Home", "lots": lots})

