# Generated by Django 4.0.5 on 2022-07-01 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL адрес категории')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='home.category')),
            ],
            options={
                'verbose_name': 'Создание категории',
                'verbose_name_plural': 'Создание категорий',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL адрес товара')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('available', models.BooleanField(default=True, verbose_name='Доступность товара')),
                ('is_published', models.BooleanField(default=True, verbose_name='Показывать на сайте?')),
                ('time_create', models.DateField(auto_now_add=True, verbose_name='Дата добавления товара')),
                ('time_update', models.DateField(auto_now=True, verbose_name='Дата загрузки товара')),
                ('image', models.ImageField(default='', upload_to='product_images/%Y-year/%m-month/%d-day/', verbose_name='Фото товара')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='images_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='home.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Создание товара',
                'verbose_name_plural': 'Создание товаров',
                'ordering': ['-time_create', 'name'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]
