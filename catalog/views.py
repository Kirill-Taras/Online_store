from typing import Any

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from catalog.models import Product, Blog


# Create your views here.

class ProductListView(ListView):
    model = Product
    extra_context = {
        "title": "Все продукты"
    }


# def home(request):
#     context = {'object_list': Product.objects.all()}
#     return render(request, "catalog/product_list.html", context)


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(
#             f"Полученные данные:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
#         )
#     return render(request, "catalog/contacts.html")


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


# def product(request, pk):
#     context = {
#         "object_list": Product.objects.get(pk=pk)
#     }
#     return render(request, "catalog/product_detail.html", context)

# class BlogCreateView(CreateView):
#     model = Blog
#     fields = ("title", "is_published")
#     success_url = reverse_lazy("catalog:blog)

class BlogListView(ListView):
    model = Blog
