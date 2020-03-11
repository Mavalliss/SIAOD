from .models import Data
from django.forms import ModelForm


class CityForm(ModelForm):
    class Meta:
        model = Data
        fields = ["name"]