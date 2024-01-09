from django import forms


class AirCityForm(forms.Form):
    city_name = forms.CharField(max_length=100, label="City")