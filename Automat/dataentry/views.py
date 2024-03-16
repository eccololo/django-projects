from django.shortcuts import render

def import_data(request):
    return render(request, template_name="dataentry/importdata.html")
