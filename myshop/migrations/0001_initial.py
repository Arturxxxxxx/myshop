# Generated by Django 5.0.6 on 2024-05-29 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Цена')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('crreated_at', models.DateTimeField(auto_now_add=True)),
                ('in_stock', models.BooleanField(default=True, verbose_name='вланичии')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='myshop.category', verbose_name='Категория')),
            ],
        ),
    ]
