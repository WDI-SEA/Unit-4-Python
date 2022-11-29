from django import forms
from django.forms import ModelForm
from .models import Feeding
class dateInput(forms.DateInput):
    input_type = 'date'
class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
    widgets={
        'date':dateInput()
    }