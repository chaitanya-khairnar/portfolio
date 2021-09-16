from django.shortcuts import render
from .models import About

def home(request):
    about = About.objects.get()

    return render(request, 'home/home.html', {
        'about' : about
    })
