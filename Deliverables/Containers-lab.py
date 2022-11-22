#Exercise 1

students = ['Jack', 'John' , 'James']
print(students[1])
print(students[-1])

#Exercise 2

foods = ('SeaFood' , 'Steak' , 'Mandi')

for food in foods:
    print(f"{food} is a good food")
    
# Exercise 3

for food in foods[-2:]:
    print(food)
    
# Exercise 4

# "I was born in city, state - population of population"

home_town = {'city' : 'Al Hidd' , 'state':'Muharraq' , 'population' :'65000' }
print(f"I was born in {home_town['city']} city, {home_town['state']} state - population of {home_town['population']}")

# Exercise 5
    
for key in home_town:
  print( f"{key} = {home_town[key]}" )
  
# Exercise 6

cohort = []

for idx, student in enumerate(students):
  cohort.append({
    'student': student,
    'fav_food': foods[idx]
  })
  
# print(cohort)

for x in cohort:
    print(x)
    
# Exercise 7

awesome_students = [[f"{name} is awesome!" for name in students ]]

for x in awesome_students:
  print(x, end=" ")
  
# Exercise 8

for food in foods:
    if 'F' in food:
     print(food)
  


    