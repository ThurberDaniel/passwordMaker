from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/index.html', {'password': "98uhbhjnkjoi8hg7uybu"})


def cars(request):
    return HttpResponse('<h1>cars are here</h1>')
