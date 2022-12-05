from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy
from .forms import FeedingForm

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()

  # we want to get all the toys that the cat doesn't already have so we can view them
  toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

  return render(request, 'cats/detail.html', {
    # pass the cat and feeding_form as context
    'cat': cat,
    'feeding_form': feeding_form,
    'toys': toys_cat_doesnt_have
  })

def add_feeding(request, cat_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

############################

def associate_toy(request, cat_id, toy_id):
  # to access the cat_id ... we have to include it in the associate_toy(...)
  Cat.objects.get(id=cat_id).toys.add(toy_id)

  # cat_id has to be the same name as in the detail path in urls
  # for redirect this is a must to be in the models file:
  # def get_absolute_url(self):
  #   return reverse('detail', kwargs={'cat_id': self.id})
  return redirect('detail', cat_id=cat_id)