from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        "slug": ["product_name"]
    }

    list_display = ["product_name", "price", "category", "stock", "is_available", "modified_date"]
    list_filter = ["price"]
    search_fields = ["product_name", "description"]

admin.site.register(Product, ProductAdmin)

