from django.shortcuts import render, redirect, reverse
from main.forms import CarEntryForm
from main.models import CarEntry
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):

    context = {
        'npm' : '2306245623',
        'name': request.user.username,
        'class': 'PBP B',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_car_entry(request):
    form = CarEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        car_entry = form.save(commit=False)
        car_entry.user = request.user
        car_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_car_entry.html", context)

def show_xml(request):
    data = CarEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CarEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = CarEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = CarEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_car(request, id):
    # Get car entry berdasarkan id
    car = CarEntry.objects.get(pk = id)

    # Set car entry sebagai instance dari form
    form = CarEntryForm(request.POST or None, instance=car)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_car.html", context)

def delete_car(request, id):
    # Get car berdasarkan id
    car = CarEntry.objects.get(pk = id)
    # Hapus car
    car.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_car_entry_ajax(request):
    car = strip_tags(request.POST.get("car")) # strip HTML tags!
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    car_horsepower = request.POST.get("car_horsepower")
    user = request.user

    new_car = CarEntry(
        car=car, description=description,
        price=price, car_horsepower=car_horsepower,
        user=user
    )
    new_car.save()

    return HttpResponse(b"CREATED", status=201)