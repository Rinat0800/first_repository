from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование категории')
    image = models.ImageField(upload_to='photos/categories/', null=True, blank=True,
                              verbose_name='Изображение категории')
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория',
        related_name='subcategories'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Company(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование компании')
    description = models.TextField(verbose_name='Описание компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование продукта')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    quantity = models.IntegerField(default=0, verbose_name='Количество на складе')
    description = models.TextField(default='Здесь скоро будет описание',
                                   verbose_name='Описание товара')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=40, verbose_name='Размер в мм')
    color = models.CharField(default='Серебрянный', verbose_name='Цвет',
                             max_length=150)
    material = models.CharField(default='Серебро', verbose_name='Материал товара',
                                max_length=150)

    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания продукта')

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория продукта',
                                 related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/products/', verbose_name='Изображение')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')

    def __str__(self):
        return f"{self.product.title}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения товаров'