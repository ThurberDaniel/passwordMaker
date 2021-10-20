from django.shortcuts import render
from django.http import HttpResponse


def cars(request):
    return HttpResponse('<h1>Cars here</h1>')


def home(request):
    return render(request, 'generator/index.html', {'passwords': "98u88888888kjoi8hg7uybu"})
