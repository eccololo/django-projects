from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm
import requests
import json


def home(request):

    if request.method == "POST":
        ticker = request.POST['ticker']
        public_token = "pk_47ea754a042d4a80afaae8e3b0ba39a4"
        api_endpoint = f"https://api.iex.cloud/v1/data/core/quote/{ticker}?token={public_token}"
        response = requests.get(api_endpoint)
        try:
            api_data = json.loads(response.content)
            api_data = api_data[0]
            if api_data is None:
                api_data = "Error"
        except Exception as e:
            api_data = "Error"
        return render(request, template_name="base.html", context={'api_data': api_data})
    else:
        return render(request, template_name="base.html", context={'ticker': "Use search for finding stocks info."})


def about(request):
    return render(request, template_name="about.html", context={})

def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added!")
            return redirect("add_stock")
    else:
        ticker = Stock.objects.all()
        return render(request, template_name="add_stock.html", context={"ticker": ticker})
