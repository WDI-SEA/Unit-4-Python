from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    success_url = '/cats/'

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url='/cats/'


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})



def cats_index(request):
    cats_list = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats_list
    })


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1> About the CatCollector </h1>')

# function home(req,res)
def home(request):
    return render(request, 'home.html')


# def home(request):
#     return HttpResponse('<h1>My First Django Route!</h1>')