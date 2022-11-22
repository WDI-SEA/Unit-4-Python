# Lab1 - The Movie Database

movies=[
    {'title': 'Bullet Train','duration': 90,'stars':'Brad Pit, Aaron Taylor'},
    {'title':'Top Gun Mavrick','duration': 120,'stars':'Tom Cruise, Miles Teller'},
    {'title': 'The Grey Man','duration': 150,'stars':'Ryan Gosling, Chris Evans'}
       ]

for mov in movies:
    print(f"{mov['title']} lasts for {mov['duration']} minutes.  Stars: {mov['stars']}")
        
# Lab2 - The Reading List

books=[
    {'title': 'The Hobbit','author': 'by J.R.R. Tolkien.','alreadyRead': True},
    {'title': 'The Lord Of Rings','author': 'by J.R.R. Tolkien.','alreadyRead': True},
    {'title': 'In Search of Lost Time','author': 'by Marcel Proust','alreadyRead': False},
      ]

for book in books:
    print(f"{book['title']}, by {book['author']}")
    
for book in books:
    if book['alreadyRead'] is True:
        print(f"You already read {book['title']} by {book['author']}")
    else:
        print(f"You still need to read {book['title']} by {book['author']}")