from django.shortcuts import render, redirect
from django.conf import settings
from django.core.management import call_command
from .utils import get_all_custom_models
from uploads.models import Upload
import platform

def import_data(request):
    if request.method == "POST":
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")

        # Store file in Upload model.
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        # Create relative path to uploaded file.
        relative_file_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)

        # Path fix for Windows users.
        if platform.system() == "Windows":
            base_url = base_url.replace('\\', '/')

        full_file_path = base_url + relative_file_path

        try:
            # Trigger the data import command.
            call_command('importdata', full_file_path, model_name)
        except Exception as e:
            raise e

        return redirect("import_data")
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models
        }
    return render(request, template_name="dataentry/importdata.html", context=context)
