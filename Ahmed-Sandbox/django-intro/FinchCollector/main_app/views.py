from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Bird():
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

birds_list = [
    Bird('Tweety', 'Brambling', 'Similar in size and shape to the chaffinch, the male has a black head in summer, and an orange breast with white belly. In flight it shows a long white rump.', 3),
    Bird('Bull', 'Bullfinch', 'The male is unmistakable with his bright pinkish-red breast and cheeks, grey back, black cap and tail, and bright white rump.', 5),
    Bird('Chaf', 'Chaffinch', 'The chaffinch is the UK\'s second commonest breeding bird, and is arguably the most colourful of the UK\'s finches.', 1),
    Bird('Goldy', 'Goldfinch', 'A highly coloured finch with a bright red face & yellow wing patch. Sociable, often breeding in loose colonies, they have a delightful liquid twittering song.', 2),
]
        

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):

    context = {
        'birds': birds_list
    }

    return render(request, 'birds/index.html', context)