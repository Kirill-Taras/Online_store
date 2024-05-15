from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Blog, Version
from catalog.services import get_product_from_cache


# Create your views here.
class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"
    extra_context = {"title": "Контакты"}


class ProductListView(ListView):
    model = Product
    extra_context = {"title": "Все продукты"}
    template_name = "catalog/product_list.html"

    def get_queryset(self):
        return get_product_from_cache


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Создать новый продукт"

        return context_data

    def get_success_url(self):
        return reverse("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Внести изменения в продукт"
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('catalog.set_published_product') and
                user.has_perm('catalog.change_description_product') and
                user.has_perm('catalog.change_category_product')):
            return ProductModeratorForm
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Удалить продукт"

        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_queryset(self):  #-> Product.query.QuerySet[_M]
        queryset = super().get_queryset()

        return queryset

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get("pk"))
        context_data["pk"] = product_item.pk
        context_data["title"] = f'Все о продукте {product_item.name}'
        activ_version = product_item.version_set.filter(current_indicator=True).first()
        context_data["activ_version"] = activ_version

        return context_data


class BlogListView(ListView):
    model = Blog
    extra_context = {"title": "Блог о еде"}

    def get_queryset(self):  #-> Product.query.QuerySet[_M]
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published")

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Создать новый блог"

        return context_data

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save(commit=False)
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview", "is_published")

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Внести изменения в блог"

        return context_data

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save(commit=False)
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("catalog:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)
        context_data["title"] = "Удалить блог"

        return context_data


class BlogDetailView(DetailView):
    model = Blog

    def get_queryset(self):  #-> Product.query.QuerySet[_M]
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))

        return queryset

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Blog.objects.get(pk=self.kwargs.get("pk"))
        context_data["pk"] = product_item.pk
        context_data["title"] = f'Подробно о {product_item.title}'

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object
