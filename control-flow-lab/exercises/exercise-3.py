age = int(input("Input a dog's age in human years: "))
if(age <= 2):
   age = age*10
else:
    age = 20 + (age-2)*7

print(f"The dog's age in dog years is {age}.")