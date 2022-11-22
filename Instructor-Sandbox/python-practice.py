# print("Hello World!!!")
"""
I can write a 
Multi line comment
"""

# my_number = 10

# print(type(str(my_number)))



# state = "Hawaii"

# year = 1959

# message = f"{state} was the last state to join the U.S. in {year}"

# print(message)



# split_string = "ace of spades".split("a")

# print(split_string)

# alphabet = "abcde"

# print(list(alphabet))



# index_of_x = "abcdqqxzzz".replace("z", "a")

# print(index_of_x)




# print(len("green eggs and ham"))






# string = "abcdefg"

# print(string[-2])


# num = 25

# # msg = "There are " + str(num) + " tacos"
# msg = "There are {}, {} tacos".format(num, "30")

# # new_msg = f"There are {num} tacos"
# print(msg)


# hex = a5

# print(int("a5", 16))

# if 1 == "1" #IN PYTHON, FALSE

# if num > 5 && num < 10 # IN JS

# if num > 5 and num <10 # PYTHON




# floor = "clean"
# walls = "sticky"

# if floor == "sticky": #:::::::::::
#     print("Clean the floor! It is sticky!")
# elif walls == "sticky":
#     print("Clean your walls!")
# else: #Optional
#     print("Your floor and walls are clean!")



# if walls:

#     print("Clean the walls! They're sticky!")
# color = ""
# while color != 'quit':
#     color = input('Enter "green", "yellow", "red": ').lower()
#     print(f'The user entered {color}')
#     if color == 'green':
#         print('Go')
#     elif color == 'yellow':
#         print('Slow Down')
#     elif color == 'red':
#         print('Stop!')
#     else:
#         print('Bogus!!!')

# names = ['Alex', 'Kareem', 'Nahid', 'Ahlam']

# for el in names:
#     print(el)




# print(type(range(5)))
# for num in range(2,11,4):
#     print(num)


# nums = tuple(range(5, 0, -1))
# print(nums)

# if 25 and 0:
#     print('True!')



# Lab : 


#1
# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# def sum_to(n):
#     total = n * (n + 1) // 2
#     print(f"The sum of the integers from 1 to {n} is {total}")

# sum_to(6)
# sum_to(10)



# # #2
# # Write a function named largest that takes a list of numbers as an argument and returns 
# # the largest number in that list.


# def largest(list):
#     largest_num = max(list)
#     print(f"Largest number is {largest_num}")

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231


#3
# Write a function named occurances that takes two string arguments as input and counts the number of occurances 
# of the second string inside the first string.


# def occurances(string, substr):
#   return print(string.count(substr))

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

#4
# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# def product(*args):
#     multiply = 1
#     for m in args:
#         multiply *= m
#     return (print(f"Product of given numbers is {multiply}"))

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0


