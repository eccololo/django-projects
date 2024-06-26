from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        "slug": ["product_name"]
    }

    list_display = ["product_name", "price", "discount", "category", "stock", "modified_date", "is_available"]
    list_filter = ["is_available", "discount"]
    search_fields = ["product_name", "description"]

admin.site.register(Product, ProductAdmin)

