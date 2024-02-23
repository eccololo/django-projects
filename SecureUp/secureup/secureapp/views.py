from django.shortcuts import render

def home(request):
    return render(request, template_name="index.html")

def register(request):
    return render(request, template_name="register.html")

def dashboard(request):
    return render(request, template_name="dashboard.html")
