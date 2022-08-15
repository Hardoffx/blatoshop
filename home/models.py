from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    """Класс категорий товаров магазина"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    # name = RichTextField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL адрес категории')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('category', kwargs=kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Создание категории'
        verbose_name_plural = 'Создание категорий'


class SystemCategories(models.Model):
    """Класс системные категории"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL адрес категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # kwargs = {'slug': self.slug}
        return '/%s/' % self.slug
        # return reverse('system_categories', kwargs=kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Системные категории'
        verbose_name_plural = 'Системные категории'


class HomeSlider(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название слайда', blank=True)
    image_1 = models.ImageField(upload_to='slider_images/%Y-year/%m-month/%d-day/', default='', verbose_name='Фото слайда 1')
    image_2 = models.ImageField(upload_to='slider_images/%Y-year/%m-month/%d-day/', default='', verbose_name='Фото слайда 2')

    def __str__(self):
        return self.name


class Product(models.Model):
    """Класс добавления товаров"""
    category = models.ManyToManyField(Category, related_name='products', verbose_name='Категории', default='')

    name = models.CharField(max_length=2000, verbose_name='Название товара')
    slug = models.SlugField(max_length=2500, unique=True, verbose_name='URL адрес товара')
    description = RichTextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Доступность товара')
    author = models.ForeignKey(User, related_name='images_author',
                               on_delete=models.CASCADE, default='',
                               verbose_name='Автор'
                               )
    is_published = models.BooleanField(default=True, verbose_name='Показывать на сайте?')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата добавления товара')
    time_update = models.DateField(auto_now=True, verbose_name='Дата загрузки товара')

    image_title = models.ImageField(
        upload_to='product_images/%Y-year/%m-month/%d-day/',
        verbose_name='Фото товара 600 x 600',
        default='',
        blank=True
    )

    image_1 = models.ImageField(
        upload_to='product_images/%Y-year/%m-month/%d-day/',
        verbose_name='Фото товара 2294 x 1947',
        default='',
        blank=True
    )
    image_2 = models.ImageField(
        upload_to='product_images/%Y-year/%m-month/%d-day/',
        verbose_name='Фото товара 2294 x 1947',
        default='',
        blank=True
    )
    image_3 = models.ImageField(
        upload_to='product_images/%Y-year/%m-month/%d-day/',
        verbose_name='Фото товара 2294 x 1947',
        default='',
        blank=True
    )

    def get_absolute_url(self):
        # return ("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})
        return f'category/{self.category.slug}/{self.slug}'
        # kwargs = {'slug': self.slug}
        # return reverse('product_detail', kwargs=kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Создание товара'
        verbose_name_plural = 'Создание товаров'
        ordering = ['-time_create', 'name']
        index_together = (('id', 'slug'),)


class ContactModel(models.Model):
    name = models.CharField('Ваше имя', max_length=150, blank=True)
    email = models.EmailField('Ваш номер телефона', blank=True)
    title = models.CharField('Предмет обращения', max_length=200, blank=True)
    message = models.TextField('Сообщение', max_length=5000, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявки из CONTACT'
        verbose_name_plural = 'Заявки из CONTACT'

    def __str__(self):
        return f'{self.name} - {self.email}'