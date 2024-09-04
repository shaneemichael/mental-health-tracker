from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306259976',
        'name': 'Shane Michael Tanata Tendy',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)