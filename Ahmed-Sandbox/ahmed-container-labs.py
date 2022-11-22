# Exercise 1
print('Exercise 1')
students=["Alya","Alex","salman", "Ahmed", "ibtisam"]
print(students[1])
print(students[-1])

# Exercise 2
print('\nExercise 2')
foods = ('Pizza', 'Fries', 'Steak', 'Burgers', 'Cola')
for food in foods:
    print(f"{food} is a good food.")


# Exercise 3
print('\nExercise 3')
for idx, food in enumerate(foods):
    if idx == len(foods)-1 or idx == len(foods)-2:
        print(f"{food}")

 
# Exercise 4
print('\nExercise 4')
home_town = {
    'city': 'New York City',
    'state': 'New York',
    'population': 1_555_199, 
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

        
# Exercise 5
print('\nExercise 5')
for key in home_town:
    print(f"{key} = {home_town[key]}")


# Exercise 6
print('\nExercise 6')
cohort = []
for i in range(0, 5):

    student = {
        'student': students[i],
        'fav_food': foods[i]
        }
    cohort.append(student)
    print

for student in  cohort:
    print(student)


# Exercise 7
print('\nExercise 7')
awesome_students = [f"{student} is awesome!" for student in students]

for awesome in awesome_students:
    print(awesome)

    
# Exercise 8
print('\nExercise 8')
food_with_a = [food for food in foods if 'a' in food]
for food in food_with_a:
    print(food)