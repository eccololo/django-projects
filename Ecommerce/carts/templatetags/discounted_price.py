from django import template
register = template.Library()


def prepare_discount(discount):
    return (100 - discount) / 100

@register.simple_tag()
def calculate_discounted_price(discounted_price, discount):
    output = int(discounted_price * prepare_discount(discount))
    return output