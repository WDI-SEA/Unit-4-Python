# Lab 1: The Movie Database - Python Dictionary

movies=[
    {'title': 'Kill Bill: Volume 1',
    'duration': 120,
    'stars': ['Uma Thurman', 'David Carradine', 'Lucy Liu']
    },

    {'title':'Back to the Future',
    'duration': 120,
    'stars': ['Michael J. Fox', 'Christopher Lloyd']
    },

    {'title': 'The Island',
    'duration': 125,
    'stars': ['Ewan McGregor', 'Scarlett Johansson', 'Steve Buscemi']}
]

for mov in movies:
    print(f"{mov['title']} lasts for {mov['duration']} minutes. Stars: {', '.join(mov['stars'])}.")


print('-------------------------------------------------------')
# Lab 2: The Reading List - Python Dictionary

books=[
    {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald’s ', 'already_read':True},
    {'title':'The Expanse', 'author':'James Corey', 'already_read':True},
    {'title':'Maze Runner', 'author':'James Dashner', 'already_read':False}
]

for book in books:
    print(f"{book['title']} by {book['author']}.")

for book in books:
    if book['already_read'] is True:
        print(f"You already read \"{book['title']}\" by {book['author']}")
    else:
        print(f"You still need to read \"{book['title']}\" by {book['author']}")