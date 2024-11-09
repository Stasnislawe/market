from django.db import models
from django.urls import reverse
from PIL import Image
from .utils import unique_slugify

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                        kwargs={'cat_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save()
        with Image.open(self.image.path) as img:
            i0, i1 = img.size
            if i0 != i1:
                if i0 > i1:
                    res = i0 - i1
                    r2 = res / 2
                    r3 = i1 + r2
                    cropped_img = img.crop((r2, 0, r3, i1))
                elif i1 > i0:
                    cropped_img = img.crop((0, 0, i0, i0))
            else:
                cropped_img = img
            cropped_img.save(self.image.path)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_detail',
                       kwargs={'prd_slug': self.slug})

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name="Дополнительные Фотографии")

    def save(self, *args, **kwargs):
        super().save()
        with Image.open(self.images.path) as img:
            i0, i1 = img.size
            if i0 != i1:
                if i0 > i1:
                    res = i0 - i1
                    r2 = res / 2
                    r3 = i1 + r2
                    cropped_img = img.crop((r2, 0, r3, i1))
                elif i1 > i0:
                    cropped_img = img.crop((0, 0, i0, i0))
            else:
                cropped_img = img
            cropped_img.save(self.images.path)
        super().save(*args, **kwargs)