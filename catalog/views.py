from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.


def home(request):
    context = {'object_list': Category.objects.all()}
    return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"Полученные данные:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
        )
    return render(request, "catalog/contacts.html")


def product(request, pk):
    context = {
        "object_list": Product.objects.get(pk=pk)
    }
    return render(request, "catalog/product.html", context)
