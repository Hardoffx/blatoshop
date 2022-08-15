from django import template
from home.models import *

register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return get_all_categories()


@register.simple_tag()
def get_system_categories():
    return SystemCategories.objects.all()