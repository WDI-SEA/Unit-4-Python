from django.shortcuts import render
from .models import Cat


# View functions

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})

def cats_index(request):
  cat_list = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cat_list })

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


