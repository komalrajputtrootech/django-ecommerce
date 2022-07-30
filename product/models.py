from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name", editable=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

