from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cheetah
from .forms import FeedingForm
# Create your views here.


# function home(req,res)
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cheetahs_index(request):
    cheetahs = Cheetah.objects.all()
    return render(request, 'cheetahs/index.html', { 'cheetahs': cheetahs })


def cheetahs_detail(request, cheetah_id):
  cheetah = Cheetah.objects.get(id=cheetah_id)
  feeding_form = FeedingForm()
  
  return render(request, 'cheetahs/detail.html', { 'cheetah': cheetah,'feeding_form': feeding_form})

class CheetahCreate(CreateView):
  model = Cheetah
  fields = '__all__'
  success_url = '/cheetahs/'
  
class CheetahUpdate(UpdateView):
  model = Cheetah
  # Let's disallow the renaming of a Cheetah by excluding the name field!
  fields = ['breed', 'description', 'age', 'image']
  success_url = '/cheetahs/'

class CheetahDelete(DeleteView):
  model = Cheetah
  success_url = '/cheetahs/'
  
def add_feeding(request, cheetah_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cheetah_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cheetah_id = cheetah_id
    new_feeding.save()
  return redirect('detail', cheetah_id=cheetah_id)