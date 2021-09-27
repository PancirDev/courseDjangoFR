from django.shortcuts import render


def home(request):
    name = 'Kler'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'About text'
    return render(request, 'about.html', {'name': name})
