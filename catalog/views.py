from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def home(request):
    context = {'object_list': Product.objects.all()}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"Полученные данные:\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}"
        )
    return render(request, "contacts.html")


def product(request, pk):
    context = {
        "object_list": Product.objects.get(pk=pk)
    }
    return render(request, "product.html", context)
