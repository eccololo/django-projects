from django.shortcuts import render


def render_home(request):
    return render(request, template_name="home.html", context={})

def render_about(request):
    return render(request, template_name="about.html", context={})
