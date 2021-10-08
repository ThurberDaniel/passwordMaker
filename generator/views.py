from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/index.html', {'passwords': "98uhbhjnkjoi8hg7uybu"})


def cars(request):
    return HttpResponse('<h1>Cars are here</h1>')
