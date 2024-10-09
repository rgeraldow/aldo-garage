from django.forms import ModelForm
from main.models import CarEntry
from django.utils.html import strip_tags

class CarEntryForm(ModelForm):
    class Meta:
        model = CarEntry
        fields = ["name", "price", "description", "car_horsepower"]
    
    def clean_car(self):
        car = self.cleaned_data["car"]
        return strip_tags(car)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)