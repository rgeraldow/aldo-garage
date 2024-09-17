from django.forms import ModelForm
from main.models import CarEntry

class CarEntryForm(ModelForm):
    class Meta:
        model = CarEntry
        fields = ["name", "price", "description", "car_horsepower"]