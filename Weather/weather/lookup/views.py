from django.shortcuts import render
from .forms import AirCityForm
import requests
import json


def view_home(request):

    air_quality_colors = {
        -1: 'gray',
        0: 'lightgreen',
        1: 'green',
        2: 'darkgreen',
        3: 'orange',
        4: 'red',
        5: 'darkred'
    }

    city_name = None
    city_id = None
    air_quality_level = "Unknown"
    air_quality_level_name = "Unknown"
    not_found_msg = ""

    # Air Quality APIs from GIOS in Poland.
    gios_endpoint_all_stations = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    response_all = requests.get(gios_endpoint_all_stations, timeout=3)

    try:
        api_content_all_stations = json.loads(response_all.content)
    except Exception as e:
        api_content_all_stations = "Some error occurred. Contact admin."

    if request.method == 'POST':
        air_city_form = AirCityForm(request.POST)
        if air_city_form.is_valid():
            city_name = air_city_form.cleaned_data['city_name']
    else:
        air_city_form = AirCityForm()  # An unbound form

    if city_name:
        for response_all_item in api_content_all_stations:
            if city_name in response_all_item['stationName']:
                city_id = response_all_item['id']
                break
        if city_id:
            gios_endpoint_one_station = f"https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{city_id}"
            response_one = requests.get(gios_endpoint_one_station, timeout=3)

            try:
                api_content_one_station = json.loads(response_one.content)
                air_quality_level = api_content_one_station['stIndexLevel']['id']
                air_quality_level_name = api_content_one_station['stIndexLevel']['indexLevelName']
            except Exception as e:
                api_content_one_station = "Some error occurred. Contact admin."
        else:
            api_content_one_station = "Data for this city not found."
    else:
        city_name = "Uknown"

    if air_quality_level == "Unknown" and air_quality_level_name == "Unknown":
        not_found_msg = "No data found for this city."

    try:
        color = air_quality_colors[air_quality_level]
    except Exception:
        color = 'gray'

    return render(request, template_name="home.html", context={
        # 'api_content_one': api_content_one_station,
        # 'api_content_all': api_content_all_stations,
        'air_city_form': air_city_form,
        'city_name': city_name,
        'air_level': air_quality_level,
        'air_quality': air_quality_level_name,
        'color': color,
        'not_found_msg': not_found_msg
    })


def view_about(request):
    return render(request, template_name="about.html", context={})
