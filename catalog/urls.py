from django.urls import path
from catalog.views import ProductListView, ContactsView, ProductDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/detail/", BlogDetailView.as_view(), name="blog_detail"),
]
