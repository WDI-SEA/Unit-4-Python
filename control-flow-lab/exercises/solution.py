

#Solution 1

letter = input('Enter a letter of the alphabet').lower()
if letter in ["a","e","i","u","o"]:
    print(f'{letter} is a Vowel.')
else:
    print(f'{letter} is a Consonant.')



#Solution 2

phrase = ""
while (phrase!="quit"):
    phrase = input("Please enter a word or phrase:")
    
    print(f"What you entered is" + str(len(phrase)) + " characters long")



#Solution 3

dog_age = input('Input a dog\'s age in human years: ')

dog_age = int(dog_age)

human_years = 0

for dog_age_el in range(1, dog_age+1):

    if dog_age_el == 1 or dog_age_el == 2:
        human_years +=10

    else:
        human_years +=7

print(f"The dog's age in dog years is {human_years}")


#Solution 4

firstLength = input('a: ')
print(f'The user entered {firstLength}')

secondLength = input('b: ')
print(f'The user entered {secondLength}')

thirdLength = input('c: ')
print(f'The user entered {thirdLength}')


if firstLength == secondLength == thirdLength:
    print(f'A triangle with sides of {firstLength},{secondLength },{thirdLength} is a equalateral triangle')
elif firstLength != secondLength  and firstLength != thirdLength  and  secondLength != thirdLength :
    print(f'A triangle with sides of {firstLength},{secondLength },{thirdLength} is a scalene triangle')

elif firstLength==secondLength or secondLength==thirdLength or firstLength==thirdLength:
 print(f'A triangle with sides of {firstLength},{secondLength },{thirdLength} is a isosceles triangle')




#Solutiion 5


# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# another solution 
# first_50 = list(range(0, 50, 1))

# index = 0
# number = 0

# while index < len(first_50):

#     if index == 0:
#         number = 0
#         print(f"term: {index} / number: {number}")

#     elif index == 1:
#         number = 0+1
#         print(f"term: {index} / number: {number}")
#     else:
#         number = first_50[index-1]+first_50[index-2]
#         print(f"term: {index} / number: {number}")

#     index += 1


       #Solution 6



