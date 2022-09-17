from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from cart.forms import CartAddProductForm

from django.contrib import messages
from .forms import ContactForm
from .models import *


class HomeView(ListView):
    model = Product
    template_name = 'home/index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['system_categories'] = SystemCategories.objects.all()
        context['slider'] = HomeSlider.objects.all()
        context['product_v'] = Product.objects.filter(category__slug='top').filter(is_published=True)
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True).filter(category__slug='iphone')


class ProductList(ListView):
    model = Product
    template_name = 'home/prod_list.html'
    context_object_name = 'prod_list'
    slug_url_kwarg = 'prod_list_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(category__slug=self.kwargs['category_slug'])
        # context['category'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'home/product_views.html'
    context_object_name = 'product'   # определяем то как будет именоваться наш обект в шаблоне
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


# class ContactView(ListView):
#     model = ContactModel
#     template_name = 'home/contact.html'
#     slug_url_kwarg = 'contact_slug'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['contact_form'] = ContactForm()
#         return context


def contact(request):

    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, 'Сообщение успешно отправлено!')
            return HttpResponseRedirect('/contact/')
    else:
        f = ContactForm()
    return render(request, 'home/contact.html', {'form': f},)


def account(request):
    return render(request, 'home/account.html')


def support(request):
    return render(request, 'home/support.html')


# def checkout(request):
#     return render(request, 'home/checkout.html')
