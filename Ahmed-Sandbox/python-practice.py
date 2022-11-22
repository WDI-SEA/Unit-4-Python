# # state = "Tokyo"

# # year = 1990

# # message = f"{state} in {year} was a great year"

# # print(message)


# # split_str = "ace of spades".split("a")

# # print(split_str)

# # alphabeat = "abcde"

# # print(list(alphabeat))


# # index_of_x = "abcdeqqqxxzz".replace("z", "a")

# # print(index_of_x)

# # print(len("eggs an cream"))


# string = "ABCDEFGHIJKLMNOPQRSTUVWQXYZ"

# print(string[-2])


# num = 25
# msg = "There are " + str(num) + " tacos"

# print(msg)

# # con = int(0xa5, 16)

# # print(0xa5)




"""
If green is entered, print the message Go!
If yellow is entered, print the message Slow Down!
If red is entered, print the message Stop!
If anything else is entered, print the message Bogus!
"""

# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')

# if color == "green":
#     print("Go!")
# elif color == "yellow":
#     print("Slow Down!")
# elif color == "red":
#     print("Stop!")
# else:
#     print("Bogus!")




# names = ['Ahmed', 'Josh', 'Alex', 'Dio']

# for name in names:
#     print(name)

# color = " "

# while color.lower() != 'quit':

#     color = input('Enter "green", "yellow", "red": ').lower()

#     print(f'The user entered {color}')

#     if color == "green":
#         print("Go!")
#     elif color == "yellow":
#         print("Slow Down!")
#     elif color == "red":
#         print("Stop!")
#     else:
#         print("Bogus!")


# for num in range(2, 11, 4):
#     print(num)

# nums = list(range(5, 0, -1))

# print(nums)


# def fahr_to_kelvin(temp):
#     return ((temp - 32) * (5/9) + 273)

# print(fahr_to_kelvin(100))

# def something():
#     return "String"

# string = something()

# print(string)


# List
# numbers = [1, 3, 2, 6, 5]

# # lambda is like def

# odds = list(filter(lambda num: num%2, numbers))


# print(odds)


# No Hoisting in Python which calling a function then declaring it below


# args ---> arguments
# kwargs ---> keyword arguments


# def add(a, b, *args, **kwrgs):


#     print(type(args))

#     for eachArg in args:
#         print(eachArg)
    
#     print(args)
#     print(kwrgs)
#     return a + b


# print(add(5,2,3,4,4,5,65,6, name="alex", music="rock"))
    

# def printName(**kwrgs):

#     for key, value in kwrgs.items():
#         print(f'key: {key} and value: {value}')

# print(printName(name="alex", music="rock"))


# str = "ahmed " + "cool"

# print(str)




# Practice

# Q1
def sum_to(n):
    print(n*(n+1)//2)
    return n*(n+1)//2

print('Q1-----')
sum_to(6)  # returns 21
sum_to(10) # returns 55


# Q2
def largest(ls):
    print(max(ls))
    return max(ls)

print('Q2-----')
largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231


#Q3
def occurances(str1, str2):

    print(str1.count(str2))
    return str1.count(str2)

print('Q3-----')
occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0


# Q4
def product(*args):
    p = args[0]
    i = 1
    while i < len(args):
        p *= args[i]
        i +=1
    print(p)
    return p

print('Q4-----')
product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0