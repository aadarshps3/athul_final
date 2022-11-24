import django_filters
from django import forms
from django_filters import CharFilter


from homeservice_app.models import seed


class SeedFilter(django_filters.FilterSet):
    customer__name = CharFilter(field_name="customer__name", label=" ",lookup_expr='icontains'
                                ,widget=forms.TextInput(attrs={"placeholder":"search customer name","class":"form-control"}))

    class Meta:
        model = seed
        fields = ("customer__name",)