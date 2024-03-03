from django.urls import path
from catalog.views import home
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="catalog"),
]
