from .models import Category

def menu_links(request):
    category_data = Category.objects.all()
    return dict(links=category_data)