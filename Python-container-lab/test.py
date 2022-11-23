student_names=['Ali','Hassan','Majed']
print(student_names[1], student_names[-1])
# ex2
foods =("Banana","Broccoli","Strawberry jam")
for x in foods:
    print(f"food {x} is a good food")
# ex3
for x in range(-2,0,1):
    print(foods[x])
# 4
home_town = {"city":"Manama","state":"Al Manamah","population":'50,000'}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
#5
for x in home_town.keys():
    print(f"{x}:{home_town[x]}")
#6
cohort =[]
i=0
for x in student_names:
    cohort.append({'student': x, 'fav_food':foods[i]})
    i+=1
    print(cohort)

#7
newList =[f"{n} is awesome" for n in student_names]
print(newList)
#8
contain_A = [x for x in foods if 'a'  in x]
print(contain_A)
