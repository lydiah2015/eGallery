from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def today_photos(request):
    images = Image.objects.all()
    return render(request, 'all-photos/today-photos.html', {"images": images},)


def search_results(request):

    if 'Name' in request.GET and request.GET["Name"]:
        search_term = request.GET.get("Name")
        print(search_term)
        searched_images = Image.search_by_title(search_term)
        for images in searched_images:
            print(images.Description)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message": message})
