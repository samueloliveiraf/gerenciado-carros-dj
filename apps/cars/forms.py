from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'factory_year', 'model_year', 'value', 'plate', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
