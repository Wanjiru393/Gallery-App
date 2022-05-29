from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")


def viewPhoto(request, pk):
    return render(request,"photo.html")


def manage(request):
    return render(request,"manage.html")