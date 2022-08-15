from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('account/', account, name='account'),
    path('contact/', contact, name='contact'),
    path('support/', support, name='support'),

    path('category/<slug:category_slug>/', ProductList.as_view(), name='prod_list'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name="product_detail"),
]
