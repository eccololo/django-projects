from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home, name="home_link"),
    path('about', views.render_about, name="about_link")
]
