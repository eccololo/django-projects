from django.shortcuts import render
from .models import List


def render_home(request):
    all_items = List.objects.all()
    return render(request, template_name="home.html",
                  context={
                      'all_items': all_items
                  })

def render_about(request):
    return render(request, template_name="about.html", context={})
