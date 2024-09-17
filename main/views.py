from django.shortcuts import render, redirect
from main.forms import CarEntryForm
from main.models import CarEntry

def show_main(request):
    car_entries = CarEntry.objects.all()

    context = {
        'npm' : '2306245623',
        'name': 'Rogerio Geraldo Wibhowo',
        'class': 'PBP B',
        'car_entries': car_entries
    }

    return render(request, "main.html", context)

def create_car_entry(request):
    form = CarEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_car_entry.html", context)

