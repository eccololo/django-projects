from django.shortcuts import render
import requests
import json

def view_home(request):

    # Air Quality APIs from GIOS in Poland.
    gios_endpoint = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    response = requests.get(gios_endpoint, timeout=3)
    print(response.content)
    try:
        api_content = json.loads(response.content)
    except Exception as e:
        api_content = {"error": e}

    return render(request, template_name="home.html", context={
        'api_content': api_content
    })


def view_about(request):
    return render(request, template_name="about.html", context={})
