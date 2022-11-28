from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm



# Create your views here.

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)




class CatUpdate(UpdateView):
  model= Cat
  fields = ['breed', 'description', 'age']
  success_url ='/cats/'


class CatDelete(DeleteView):
   model= Cat
   success_url = '/cats/'



class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url='/cats/'
  
  
# function home(req,res)
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('<h1>About the CatCollector</h1>')

# def contact(request):
#     return HttpResponse('<h1>Contact Page</h1>')


# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    
    feeding_form = FeedingForm()
    
    
    return render(request, 'cats/detail.html', {
    'cat': cat,
    'feeding_form': feeding_form
    
                  })


def cats_index(request):
  
    cats_list = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats_list
    })
