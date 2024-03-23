from typing import Any

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Blog


# Create your views here.

class ProductListView(ListView):
    model = Product
    extra_context = {
        "title": "Все продукты"
    }


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):  #-> Product.query.QuerySet[_M]
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))

        return queryset

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get("pk"))
        context_data["pk"] = product_item.pk
        context_data["title"] = f'Все о продукте {product_item.name}'

        return context_data


class BlogListView(ListView):
    model = Blog
    extra_context = {
        "title": "Блог о еде"
    }


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("catalog:blog_list")
    extra_context = {
        "title": "Создать новый блог"
    }


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("catalog:blog_list")
    extra_context = {
        "title": "Внести изменения в блог"
    }


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")
    extra_context = {
        "title": "Удалить блог"
    }
