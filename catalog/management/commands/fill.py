import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Получаем список с объектами категорий"""
        list_category = list()
        with open('fixtures/category_data.json', 'r', encoding='utf-8') as f:
            categories_data = json.load(f)
            for category in categories_data:
                if category['model'] == 'catalog.category':
                    list_category.append(category)

        return list_category

    @staticmethod
    def json_read_products():
        """Получаем список с объектами продуктов"""
        list_products = list()
        with open('fixtures/category_data.json', 'r', encoding='utf-8') as f:
            categories_data = json.load(f)
            for category in categories_data:
                if category['model'] == 'catalog.product':
                    list_products.append(category)

        return list_products

    def handle(self, *args, **options):
        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category['pk'],
                    name=category['fields']['name'],
                    description=category['fields']['description']
                )
            )

        # Cоздаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append((
                Product(
                    id=product["pk"],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    picture=product["fields"]["picture"],
                    category=Category.objects.get(id=product["fields"]["category"]),
                    price=product["fields"]["price"],
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"],
                )
            )
            )
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

