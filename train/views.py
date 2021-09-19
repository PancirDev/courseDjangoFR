from django.shortcuts import render


def home(request):
    name = 'Kler'
    return render(request, 'home.html', {'name': name})


def about(request):
    abouttext = 'Text about us..'
    return render(request, 'about.html', {'abouttext': abouttext})
