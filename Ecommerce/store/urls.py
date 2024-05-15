from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    # FIXME:
    # This url doesn't work.
    path("<slug:category_slug>", views.store, name="product_by_category")
]
