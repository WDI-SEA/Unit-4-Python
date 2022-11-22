# where_my_things_are = {
#     'phone': 'kitchen',
#     'coffee cup': 'bedroom',
#     'wallet': 'garden',
# }

# print("my [key] is kept in [value]")


# players = ['Ronaldo', 'Messi', 'Neymar', 'Ahmed']

# # players.remove('Ahmed')

# for p in players:

#     print(p)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
# # I want 'n * n' for each 'n' in nums 
# squares = []
# for n in nums:
#   squares.append(n * n)
# print(squares)
# > [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# one, two, three = 'abc'
# print(two)




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
    print(f"{movie['title']} lasts for {movie['duration']} minutes. stars: {stars}")


# Lab 2

    Dictionary = [
    {
        'title': 'Gone Girl',
        'author': 'Alya',
        'alreadyRead': True
    },
    {
        'title': 'How to fly',
        'author': 'Mohamed',
        'alreadyRead': True
    },
    {
        'title': 'be a millionare in 10 minutes',
        'author': 'nathanael',
        'alreadyRead': False
    },
]

for book in Dictionary:
    print (f"{book['title']} by {book['author']}")

    if book['alreadyRead'] == True:
        print(f"you already read {book['title']} by {book['author']}")
    else:
        print(f"you still need to read {book['title']} by {book['author']}")

        

    