from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Cat

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Create your views here.

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url='/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    success_url='/cats/'

class CatDelete(DeleteView):
    model = Cat
    success_url='/cats/'


# this is a function
def home(request):
    return render(request, 'home.html')

def about(request):
    # view an HTML file
    return render(request, 'about.html')
    
    # maybe we could use the return HttpResponse for page not found ...
    # return HttpResponse('<h1>About the CatCollector</h1>')

# Sample data

# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats_list = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

def cats_index(request):

    cats_list = Cat.objects.all()

    return render(request, 'cats/index.html', {
        'cats': cats_list
    })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # cat_id we declared it with request & id is from the database colomn name

    feeding_form = FeedingForm()

    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
        })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()

    return redirect('detail', cat_id=cat_id)

# we don't have to say export in Django. It knows that by default