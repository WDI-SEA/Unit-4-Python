movieList = [{"name":'The strangers', "duration":"1hr30m", "stars":['Liv Taylor']},
    {'name':'A Bronx Tale' , "duration":"2hrs","stats":['Robert De Niro','Taral Hicks']}]

for film in movieList:
    print(f'{film["name"]} last for {film["duration"]}')

bookList=[{"title":"The catcher in the rye", "author": "J. D. Salinger", "alreadyRead": False},
{"title":"Jane Eyre", "author": "Charlotte Bronte", "alreadyRead": True}]
for book in bookList:
    if book["alreadyRead"]:
        print(f"You already read {book['title']}")
    else:
        print(f"You still haven't read {book['title']}")
        