from django.shortcuts import render, redirect
from .forms import CreateUserForm

def home(request):
    return render(request, template_name="index.html")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("two_factor:login")
    context = {"form": form}
    return render(request, template_name="register.html", context=context)

def dashboard(request):
    return render(request, template_name="dashboard.html")
