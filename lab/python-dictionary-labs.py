# Lab 1: The Movie Database - Python Dictionary 
# It's like IMDB, but much much smaller!

# Create a list of dictionaries to store the following information about your five favorite movies: title (a string), duration (a number), and stars (a list of strings).

# Print out the movie information like so:

# Puff the Magic Dragon lasts for 30 minutes. Stars: Puff, Jackie, Living Sneezes.



favorite_movies =[ 
 {
   'title': 'Black Adam',
    'duration': 120,
    'stars': ['Dwayne Johnson', 'Aldis Hodge', 'Quintessa Swindell']
 },
 {'title': 'Top Gun Maverick',
 'duration': 130, 
 'stars': ['Tom Cruise', 'Miles Teller', 'Jennifer Connelly']
 },
 {'title': 'Doctor Strange in the Multiverse of Madness ',
 'duration': 135, 
 'stars': ['Benedict Cumberbatch', 'Chiwetel Ejiofor', 'Elizabeth Olsen']
 },
 {'title': 'Enola Holmes 2',
 'duration': 130, 
 'stars': ['Milly Brown', 'Henry Cavill', 'David Thoulis']
 },
 {'title': 'Orphan First Kill',
 'duration': 90, 
 'stars': ['Isabelle Fuhrman', 'Julia Stiles', 'Rossif Sutherland']
 },
 
]

for movie in favorite_movies:
    stars = ','.join(movie['stars'])
    print(f"{movie['title']} lasts for {movie['duration']} minutes. stars: {stars}.")
   



# Lab 2: The Reading List - Python Dictionary 
# Keep track of which books you read and which books you want to read!

# Create a list of dictionaries, where each object describes a book and has properties for the title (a string), author (a string), and alreadyRead (a boolean indicating if you read it yet).

# Iterate through the list of books. For each book, log the book title and book author like so:

# "The Hobbit by J.R.R. Tolkien".

# Now use an if/else statement to change the output depending on whether you read it yet or not.

# If you read it, log a string like

# 'You already read "The Hobbit" by J.R.R. Tolkien',

# and if not, log a string like
# 'You still need to read "The Lord of the Rings" by J.R.R. Tolkien.


books =[ 
 {
   'title': 'It Ends With Us',
    'author': 'Colleen Hoover',
    'alreadyRead': True
 },
 {
   'title': 'The Old Man and the Sea ',
    'author': 'Ernest Miller Hemingway',
    'alreadyRead': False
 },
 {
   'title': 'Harry Potter and the Cursed Child: Parts One and Two',
    'author': 'John Tiffany',
    'alreadyRead': True
 },
 {
   'title': 'Dark Matter',
    'author': 'Andy Weir',
    'alreadyRead': False
 },
 
]


for book in books:
     
    if book ['alreadyRead'] == True:
      print(f"You already read {book['title']} by {book['author']}.")
    else:
      print(f"You still need to read {book['title']} by {book['author']}.") 
   

