from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245623',
        'name': 'Rogerio Geraldo Wibhowo',
        'class': 'PBP B',
        'e-commerce' : 'Aldo Garage',
        'product': 'Ferrari F40',
        'price': '2.450.000.000'
    }

    return render(request, "main.html", context)


