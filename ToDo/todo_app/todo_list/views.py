from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect


def render_home(request):
    if request.method == "POST":
        form_item = ListForm(request.POST or None)

        if form_item.is_valid():
            form_item.save()
            messages.success(request, ("Item added"))
            all_items = List.objects.all()

            return render(request, template_name="base.html",
                          context={
                              'all_items': all_items
                          })
    else:
        all_items = List.objects.all()
        return render(request, template_name="base.html",
                      context={
                          'all_items': all_items
                      })


def render_about(request):
    return render(request, template_name="about.html", context={})


def render_delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item deleted"))
    return redirect("home_link")
