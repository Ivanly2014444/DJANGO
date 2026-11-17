
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    overview = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    overview = models.TextField(blank=True, null=True, verbose_name='Описание')
    img = models.ImageField(upload_to='catalog/image',verbose_name='Изображение', blank=True, null=True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True,verbose_name='Категория')
    price_per_item = models.IntegerField(blank=True, null=True,verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name
