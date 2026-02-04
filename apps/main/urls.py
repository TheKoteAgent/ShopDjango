from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.lot_list, name="lot_list"),
    path('category/<slug:category_slug>/', views.lot_list, name="lot_list_by_category"),
    path('lot/<int:id>/', views.lot_detail, name="lot_detail")
]
