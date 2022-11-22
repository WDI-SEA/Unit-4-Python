# Python
# Lab 1
favorite_movies = [
    {
        'title': 'Gone Girl',
        'duration': 120,
        'stars': ['Ben Affleck', 'Rosamund Pike']
    },
    {
        'title': 'Inception',
        'duration': 150,
        'stars': ['Leo', 'Tom']
    },
    {
        'title': 'Jumanji',
        'duration': 90,
        'stars': ['The Rock', 'Kevin Hart']
    },
    {
        'title': 'Hangover',
        'duration': 80,
        'stars': ['Bradley Cooper', 'Zach', 'Mike']
    },
    {
        'title': 'Rush Hour',
        'duration': 90,
        'stars': ['Jackie Chan', 'Chris']
    },
]


for movie in favorite_movies:
    stars = ', '.join(movie['stars'])
    print(f"{movie['title']} lasts for {movie['duration']} minutes. Stars: {stars}.")

    



    

# Lab 3

Dictionaries = [
    {
        'title': 'Gone Girl',
        'author': 'Alya',
        'alreadyRead': True
    },
   {
        'title': 'Biill',
        'author': 'Ahmed',
        'alreadyRead': True
    },
	{
        'title': 'Gon',
        'author': 'Salman',
        'alreadyRead': True
    },
]

for book in Dictionaries:
	print(f"{book['title']} by {book['author']}")


	if book['alreadyRead'] == True:
		print(f"You already read {book['title']} by {book['author']}")
	else:
		print(f"You still need to read \"{book['title']}\" by {book['author']}.")
		
		
		

