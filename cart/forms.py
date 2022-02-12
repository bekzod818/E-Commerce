from django import forms
from django.utils.translation import gettext_lazy as _


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label=_('Quantity'), min_value=1, max_value=20)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
