from django.db import models
from store.models import Product

class Cart(models.Model):

    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def discounted_cart_price(self):
        return int(self.product.price * ((100 - self.product.discount) / 100))
    
    def discounted_cart_sub_total_price(self):
        return int(self.sub_total() * ((100 - self.product.discount) / 100))