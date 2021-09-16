from django.shortcuts import render

def home(request):
    return render(request,'experience/details.html')

def details(request):
    return render(request, 'experience/details.html')