from django.shortcuts import render
import requests
import json


def home(request):
    public_token = "pk_47ea754a042d4a80afaae8e3b0ba39a4"
    api_endpoint = f"https://api.iex.cloud/v1/data/core/quote/aapl?token={public_token}"
    response = requests.get(api_endpoint)
    try:
        api_data = json.loads(response.content)
    except Exception as e:
        api_data = "Error ..."

    return render(request, template_name="base.html", context={'api_data': api_data})

def about(request):
    return render(request, template_name="about.html", context={})
