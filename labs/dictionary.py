# Lab 1: The Movie Database - Python Dictionary (40 mins)
# It's like IMDB, but much much smaller!

# Create a list of dictionaries to store the following information about your five favorite movies: title (a string), duration (a number), and stars (a list of strings).

# Print out the movie information like so:

# Puff the Magic Dragon lasts for 30 minutes. Stars: Puff, Jackie, Living Sneezes.

movies = [{
  'movie': 'harry poter',
  'duration': 120,
  'stars': 'Daniel Radcliffe, '+'Rubert Grint, '+'Emma Watson'
},
{
  'movie': 'Titanic',
  'duration': 180,
  'stars': 'Leonardo Dicaprio, '+'Kate Winslet, '+'Billy Zane'
},
{
  'movie': 'Black Panther',
  'duration': 120,
  'stars': 'Chadwick Boseman, '+'Lupita Nyong, '+'Michael B.Jordan'
}]

for idx, m in enumerate(movies):
    print(f"{movies[idx]['movie']} lasts for {movies[idx]['duration']} minutes. Stars: {movies[idx]['stars']}.")

###########################################
print("")

# Lab 2: The Reading List - Python Dictionary (40 mins)
# Keep track of which books you read and which books you want to read!

# Create a list of dictionaries, where each object describes a book and has properties for the title (a string), author (a string), and alreadyRead (a boolean indicating if you read it yet).

# Iterate through the list of books. For each book, log the book title and book author like so:

# "The Hobbit by J.R.R. Tolkien".

# Now use an if/else statement to change the output depending on whether you read it yet or not.

# If you read it, log a string like

# 'You already read "The Hobbit" by J.R.R. Tolkien',

# and if not, log a string like
# 'You still need to read "The Lord of the Rings" by J.R.R. Tolkien.

dictionaries = [
    {
        'title': 'The True Life',
        'author': 'Sabika',
        'Read': True
    },
   {
        'title': 'Dreams Falling',
        'author': 'Layla',
        'Read': True
    },
	{
        'title': 'Hope',
        'author': 'Ranya',
        'Read': False
    },
]
for book in dictionaries:
	print(f"{book['title']} by {book['author']}")
	if book['Read'] == True:
		print(f"You already read {book['title']} by {book['author']}")
	else:
		print(f"You still need to read {book['title']} by {book['author']}")