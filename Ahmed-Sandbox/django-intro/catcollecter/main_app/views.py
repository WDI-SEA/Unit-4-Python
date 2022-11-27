from django.shortcuts import render
from .models import Cat
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    
    cats_list  = Cat.objects.all()

    context = {
        'cats': cats_list
    }

    return render(request, 'cats/index.html', context)

def cats_details(request, cat_id):
    
    cat = Cat.objects.get(id=cat_id)

    context = {
        'cat': cat
    }
    return render(request, 'cats/details.html', context)