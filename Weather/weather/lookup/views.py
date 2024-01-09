from django.shortcuts import render


# Create your views here.

def view_home(request):
    return render(request, template_name="home.html", context={})


def view_about(request):
    return render(request, template_name="about.html", context={})
