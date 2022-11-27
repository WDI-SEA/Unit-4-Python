# Exercise 1

students = ['Tina', 'Fred', 'Wilma']
print(students[1])
print(students[-1])

# Exercise 2

foods = ['Cheeseburger', 'Pizza', 'Stuffed Bell Pepper']
for food in foods:
  print(f"{food} is a good food!")

# Exercise 3

for food in foods[-2:]:
  print(food)

# Exercise 4

home_town = {
  'city': 'Arcadia',
  'state': 'California',
  'population': 58000
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5

for key, value in home_town.items():
  print(f"{key} = {value}")

# Exercise 6

cohort = []

for index, student in enumerate(students):
  cohort.append({
    'student': student,
    'fav_food': foods[index]
  })

for student in cohort:
  print(student)

# Exercise 7

awesome_students = [f"{name} is awesome!" for name in students]

for student in awesome_students:
  print(student)

# Exercise 8

for food in [food for food in foods if 'a' in food]:
  print(food)