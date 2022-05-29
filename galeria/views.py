from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request,"index.html",context)


def viewPhoto(request, pk):
    return render(request,"photo.html")


def manage(request):
    return render(request,"manage.html")