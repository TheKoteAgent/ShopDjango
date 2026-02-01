from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('lots/', views.lot_list, name="lot_list"),
    path('<slug:category_slug>', views.lot_list, name="lot_list_by_category"),
    path('<int:id>/<slug:slug>', views.lot_list, name="lot_detail")
]
