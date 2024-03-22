from django.urls import path
from catalog.views import ProductListView, ContactsView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail")
]
