from django.shortcuts import render
from .models import Category, Photo, Location

# Create your views here.

def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos, 'locations': locations}
    return render(request,"index.html",context)



# def searchImage(request):
   
#     return render(request,"photo.html", {'photo':photo})


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,"photo.html", {'photo':photo})


def manage(request):
    categories = Category.objects.all()
    locations = Location.objects.all()

    if request.method == 'POST':

        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        if data['location'] != 'none':
            location = Location.objects.get(id=data['location'])
        elif data['location_new'] != '':
            location, created = Location.objects.get_or_create(name=data['location_new'])
        else:
            location = None

        photo = Photo.objects.create(
            category=category,
            location=location,
            description=data['description'],
            image=image,

        )

    context = {'categories': categories, 'locations':locations}
    return render(request,"manage.html", context)