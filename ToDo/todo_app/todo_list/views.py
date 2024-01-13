from django.shortcuts import render
from .models import List
from .forms import ListForm


def render_home(request):

    if request.method == "POST":
        form_item = ListForm(request.POST  or None)

        if form_item.is_valid():
            form_item.save()

            all_items = List.objects.all()

            return render(request, template_name="home.html",
                          context={
                              'all_items': all_items
                          })
    else:
        all_items = List.objects.all()
        return render(request, template_name="home.html",
                      context={
                          'all_items': all_items
                      })


def render_about(request):
    return render(request, template_name="about.html", context={})
