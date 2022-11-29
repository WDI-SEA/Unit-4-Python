from django.shortcuts import render, redirect
from .models import Finch
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
class CatCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url= '/index'
class CatUpdate(UpdateView):
  model = Finch
  fields = '__all__'
  success_url= '/index'
class CatDelete(DeleteView):
  model = Finch
  success_url= '/index'




def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def finches_index(request):
  mydata = Finch.objects.all()
  feeding_form = FeedingForm()
  return render(request, 'index.html', { 'finches':mydata,'feeding_form': feeding_form })
def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('/index')

    