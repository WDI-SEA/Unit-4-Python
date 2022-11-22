# Exercise 1
students = ['Ann', 'Youngk', 'Hyunjin', 'Sungjin', 'Wonpil', 'Dowoon']
print(students[1])
print(students[-1])

print('------------------------------------')
# Exercise 2
foods = ('Sushi', 'Ramen', 'Pizza', 'Kimpab', 'Chesse Burger', 'Fried chekin')

for item in foods:
    print(f"{item} is a good food.")

print('------------------------------------')
# Exercise 3
for item in foods[-2:]:
    print(f"{item} is a good food.")

print('------------------------------------')
# Exercise 4
home_town = {
    'city': 'New Orleans',
    'state': 'Louisiana',
    'population': '343,829'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

print('------------------------------------')
# Exercise 5
for key,value in home_town.items():
    print(f"{key} = {value}")

print('------------------------------------')
# Exercise 6
cohort = []
for idx,s in enumerate(students):
    cohort = {'student' : s, 'fav_food': foods[idx]}
    print(cohort)


print('------------------------------------')
# Exercise 7
awesome_students = []
for s in students:
    awesome_students = f"{s} is awesome!"
    print(awesome_students)

print('------------------------------------')
# Exercise 8
for food in foods:
    if("a" in food):
        print(food)