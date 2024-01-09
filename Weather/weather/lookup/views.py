from django.shortcuts import render
from .forms import AirCityForm
import requests
import json

def view_home(request):
    api_content_one_station = None
    city_name = None

    # Air Quality APIs from GIOS in Poland.
    gios_endpoint_all_stations = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    response_all = requests.get(gios_endpoint_all_stations, timeout=3)

    try:
        api_content_all_stations = json.loads(response_all.content)
    except Exception as e:
        api_content_all_stations = {"error": e}

    if request.method == 'POST':
        air_city_form = AirCityForm(request.POST)
        if air_city_form.is_valid():

            city_name = air_city_form.cleaned_data['city_name']

            gios_endpoint_one_station = "https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/114"
            response_one = requests.get(gios_endpoint_one_station, timeout=3)

            try:
                api_content_one_station = json.loads(response_one.content)
            except Exception as e:
                api_content_all_stations = {"error": e}

    else:
        air_city_form = AirCityForm()  # An unbound form

    return render(request, template_name="home.html", context={
        'api_content_one': api_content_one_station,
        'air_city_form': air_city_form,
        'city_name': city_name
    })


def view_about(request):
    return render(request, template_name="about.html", context={})
