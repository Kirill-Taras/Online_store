from django.db import models
from datetime import datetime


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    picture = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=datetime.now())
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', default=datetime.now())

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Blog(models.Model):
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    slug = models.CharField(max_length=60, unique=True, verbose_name='Слог', **NULLABLE)
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    count_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('title',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    number = models.IntegerField(verbose_name="Номер версии")
    name = models.CharField(max_length=60, verbose_name="Название версии")
    current_indicator = models.BooleanField(verbose_name="Признак текущей версии")
    verification_code = models.CharField(max_length=9, verbose_name="Код верификации", **NULLABLE)

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.number}, {self.name}'
