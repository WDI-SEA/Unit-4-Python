
# PRAINT ("HELLO WORLD!!")
"""
I can write a Multi line comment 
"""


# my_number = 15

# print(my_number)
# my_number


# If green is entered, print the message Go!
# If yellow is entered, print the message Slow Down!
# If red is entered, print the message Stop!
# If anything else is entered, print the message Bogus!

color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')
if color=='green':
    print('Go!')
elif color=='yellow':
    print('Slow down')
elif color =='red':
    print('Stop!')
else:
    print('Bogus')



    Code for control-flow-lab exercises:
# exercise 1:
letter = " "
while letter != "quit":
    letter = input('Please enter a letter from the alphabet (a-z or A-Z): ')
    
    if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is not a vowel")


        # exercise 2:
phrase = " "
while phrase != "quit":
    phrase = input('Please enter a word or phrase: ')
    
    print(f"What you entered is {len(phrase)} characters long")

    # exercise 3:
years = " "
while years != "quit":
    years = input("Input a dog's age in human years: ")
    human_years = int(years)
    
    if human_years < 0:
    	print("Age must be positive number.")
    	exit()
    elif human_years <= 2:
	    dog_years = human_years * 10
    else:
	    dog_years = 20 + (human_years - 2)*7
    
    print(f"The dog's age in dog years is {dog_years}")
exercise 4:
print("Enter the lengths of three side of a triangle:")
a = input("a: ")
b = input("b: ")
c = input("c: ")

if a == b and b == c and c == a:
	print(f"A triangle with sides of {a}, {b} & {c} is a equalateral triangle")
elif a != b and b != c and c != a:
    print(f"A triangle with sides of {a}, {b} & {c} is a scalene triangle")
else:
    print(f"A triangle with sides of {a}, {b} & {c} is a isosceles triangle")