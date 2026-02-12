from django import template
from ..models import Lot

register = template.Library()

@register.simple_tag
def get_products_count(category=None):
    if category:
        return Lot.objects.filter(category=category, is_available=True).count()
    return Lot.objects.filter(is_available=True).count()

@register.simple_tag
def calculate_total(price, quantity):
    try:
        return float(price) * int(quantity)
    except (ValueError, TypeError):
        return 0

@register.simple_tag(takes_context=True)
def user_greeting(context):
    user = context.get('user')
    if user and user.is_authenticated:
        return f"Вітаємо, {user.username}!"
    return "Вітаємо, гість!"