from django.shortcuts import render
from django.http import HttpResponse


class Finch ():
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    

Finches_list = [
    Finch('Tweety', 'Brambling', 'Similar in size and shape to the chaffinch, the male has a black head in summer, and an orange breast with white belly. In flight it shows a long white rump.', 3),
    Finch('Bull', 'Bullfinch', 'The male is unmistakable with his bright pinkish-red breast and cheeks, grey back, black cap and tail, and bright white rump.', 5),
    Finch('Chaf', 'Chaffinch', 'The chaffinch is the UK\'s second commonest breeding bird, and is arguably the most colourful of the UK\'s finches.', 1),
    Finch('Goldy', 'Goldfinch', 'A highly coloured finch with a bright red face & yellow wing patch. Sociable, often breeding in loose colonies, they have a delightful liquid twittering song.', 2),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>My First Django Route!</h1>')


def about(request):
  return render(request, 'about.html')
  # return HttpResponse('<h1>About the CatCollector</h1>')


# Add new view
def finches_index(request):
  return render(request, 'finches/index.html', { 'Finches': Finches_list  })

