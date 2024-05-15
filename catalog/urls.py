from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (ProductListView, ContactsView, ProductDetailView, BlogListView, BlogCreateView, BlogUpdateView,
                           BlogDeleteView, BlogDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/detail", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/detail/", BlogDetailView.as_view(), name="blog_detail"),
]
