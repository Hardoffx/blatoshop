# Generated by Django 3.2.5 on 2022-08-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Ваш номер телефона')),
                ('title', models.CharField(max_length=200, verbose_name='Предмет обращения')),
                ('message', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявки на Безпплатную Консультацию',
                'verbose_name_plural': 'Заявки на Безпплатныи  Консультации',
            },
        ),
    ]
