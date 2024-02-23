from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'Contactus.html')


def gallery(request):
    return render(request, 'gallery.html')
