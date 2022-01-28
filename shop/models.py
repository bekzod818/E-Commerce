from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

#
# class SubCategory(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Sub Category'
#         verbose_name_plural = 'Sub Categories'
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])
