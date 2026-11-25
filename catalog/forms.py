from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "overview", "img", "category", "price_per_item")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.required = True

    def clean_price_per_item(self):
        price = self.cleaned_data.get("price_per_item")
        if price is not None and price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля!")
        return price