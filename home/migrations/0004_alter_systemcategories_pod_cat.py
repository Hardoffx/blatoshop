# Generated by Django 4.0.5 on 2022-07-12 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactsubcat_systemcategories_pod_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemcategories',
            name='pod_cat',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='home.contactsubcat'),
        ),
    ]
