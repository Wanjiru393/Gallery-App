from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def index(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request,"index.html",context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,"photo.html", {'photo':photo})


def manage(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request,"manage.html", context)