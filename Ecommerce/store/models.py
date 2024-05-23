from django.db import models
from django.urls import reverse
from category.models import Category
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):

    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products/')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    discount = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(100)])

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    #Relation
    # FIXME:
    # 1. Change on_delete - when Category will be deleted it will dissapear from product
    #    without deleting it.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name
    
    def get_url(self):
        return reverse("product_detail", args=[self.category.slug, self.slug])