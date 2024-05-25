from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

def cart(request):
    return render(request, 'store/cart.html')



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()

    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Creating Cart
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )

    cart.save()

    # Adding Cart and Product to CartItem
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
    
    cart_item.save()

    return redirect("cart")
