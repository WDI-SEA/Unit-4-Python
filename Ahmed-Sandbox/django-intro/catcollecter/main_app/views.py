from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


# Class Based Views
class CatCreate(CreateView):
    # Specify the views
    model = Cat

    # choose all the fields
    fields  = '__all__'

    # to specify the fields
    # fields = ['name', 'breed']

    success_url = '/cats/'

    
class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    success_url = '/cats/'

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'