from django import template
register = template.Library()

@register.simple_tag()
def calculate_old_price(discounted_price, discount, *args, **kwargs):
    return int(discounted_price * (1 + (discount / 10)))