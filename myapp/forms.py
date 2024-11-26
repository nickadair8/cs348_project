from django import forms
from .models import Theme, LegoSet, Customer, Reviews

class LegoSetFilterForm(forms.Form):
    theme = forms.ModelChoiceField(
        queryset=Theme.objects.all(),
        required=False,
        empty_label="All Themes",
        label="Filter by Theme"
    )
    status = forms.ChoiceField(
        choices=[
            ('', 'All Statuses'),
            ('available', 'Available'),
            ('retired', 'Retired')
        ],
        required=False,
        label="Filter by Status"
    )
    price_range = forms.ChoiceField(
        choices=[
            ('', 'All Prices'),
            ('below_100', 'Below $100'),
            ('100_300', '$100 - $300'),
            ('300_500', '$300 - $500'),
            ('above_500', 'Above $500')
        ],
        required=False,
        label="Filter by Price"
    )

class LegoSetForm(forms.ModelForm):
    class Meta:
        model = LegoSet
        fields = ['set_id', 'name', 'piece_count', 'price', 'theme_id', 'status']

class CustomerFilterForm(forms.Form):
    budget_range = forms.ChoiceField(
        choices=[
            ('', 'All Prices'),
            ('below_100', 'Below $100'),
            ('100_300', '$100 - $300'),
            ('300_500', '$300 - $500'),
            ('above_500', 'Above $500')
        ],
        required=False,
        label="Filter by Budget"
    )
    lego_set = forms.ModelChoiceField(
            queryset=LegoSet.objects.all(),
            required=False,
            empty_label="All Sets",
            label="Filter by Set"
    )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['lego_rewards_id', 'name', 'set_id', 'budget']