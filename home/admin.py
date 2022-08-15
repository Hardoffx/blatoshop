from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(SystemCategories)
class SystemCategoriesAdmin(admin.ModelAdmin):
    """Отображение  sis-категорий в админке"""
    list_display = ['name', 'slug']
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):    # MPTTModelAdmin убрать рамки в адмнке
    """Отображение категорий в админке"""
    list_display = ['name', 'slug']
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение товаров в админке"""
    list_display = ['name', 'slug', 'id', 'available', 'is_published', 'get_image', 'time_create']
    # readonly_fields = ['get_image']
    prepopulated_fields = {'slug': ('name', 'category',)}
    list_editable = ['available', 'is_published']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_title.url} width="75" height="75"')


admin.site.register(ContactModel)
admin.site.register(HomeSlider)
# admin.site.register(SystemCategories)


