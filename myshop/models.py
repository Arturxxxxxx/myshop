from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=15, unique=True, verbose_name='Категория')
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    price = models.DecimalField(max_digits=15, decimal_places=3,verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    category = models.ForeignKey(Category, related_name='Products', on_delete=models.CASCADE, verbose_name='Категория')
    crreated_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True, verbose_name='вланичии')
    def __str__(self):
        return self.name
