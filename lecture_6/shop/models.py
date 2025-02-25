from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    price = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=False)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'ID: {self.id} {self.name}'

# Category - Categories - Categorys
