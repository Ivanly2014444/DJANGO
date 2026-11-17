from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "add products"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category = Category.objects.create(name="Овощи", overview="Свежие овощи")

        products = [
            {"name": "Помидор", "price_per_item": 200, "category": category},
            {"name": "Лук", "price_per_item": 40, "category": category},
        ]

        for products_data in products:
            new_product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully:{products_data['name']}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exist:{products_data['name']}")
                )
