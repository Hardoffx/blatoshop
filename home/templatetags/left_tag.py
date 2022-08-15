from django import template
# from home.models import *

from home.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


# @register.simple_tag()
# def get_system_categories():
#     return SystemCategories.objects.all()

