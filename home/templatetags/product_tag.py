from django import template
from home.models import *

register = template.Library()


@register.simple_tag()
def get_product():
    return Product.objects.select_related("category").order_by("-id")[:5]


# @register.inclusion_tag('include/product.html')
# def get_product():
#     prod = Product.objects.all()
#     return {'prod': prod}
