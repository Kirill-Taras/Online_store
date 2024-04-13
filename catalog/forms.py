from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ("name", "category", "price", "picture", "description")

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in ban_words:

            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError(f"Название содержит запрещенное слово: {word}")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in ban_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError(f"Описание содержит запрещенное слово: {word}")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
