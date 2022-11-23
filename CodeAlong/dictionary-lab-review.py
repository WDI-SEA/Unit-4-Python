# Lab 1

movies = [{
  'movie': 'harry poter',
  'duration': 120,
  'stars': ['Daniel Radcliffe','Rubert Grint','Emma Watson']
},
{
  'movie': 'Titanic',
  'duration': 180,
  'stars': ['Leonardo Dicaprio','Kate Winslet','Billy Zane']
},
{
  'movie': 'Black Panther',
  'duration': 120,
  'stars': ['Chadwick Boseman','Lupita Nyong','Michael B.Jordan']
}]

for idx, m in enumerate(movies):
    stars = ', '.join(m['stars'])
    print(f"{movies[idx]['movie']} lasts for {movies[idx]['duration']} minutes. Stars: {stars}.")

#################################

# Lab 2

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

for b in dictionaries:
    if b['Read']:
        print(f"You already read {b['title']} by {b['author']}")
    else:
        print(f"You still need to read {b['title']} by {b['author']}")