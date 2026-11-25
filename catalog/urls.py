from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contact, product_detail, product_create

app_name = CatalogConfig.name

urlpatterns = [
    path("", products_list, name="products_list"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("products/create/", product_create, name="product_create"),
    path("contacts/", contact, name="contact"),
]
