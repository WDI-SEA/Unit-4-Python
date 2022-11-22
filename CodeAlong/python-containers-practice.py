# student = {
#   'name': 'Maria',
#   'course': 'SEI',
#   'current_week': 7
# } 
# student['unit'] = 4 # add it to the student
# del student['unit'] # delete it from student

# student['name'] = 'Layla'
# print(student)

# if 'course' in student:
#   print( f"{student['name']} is enrolled in {student['course']}")
# else:
#   print( f"{student['name']} is not enrolled in a course")

###################################

# where_my_things_are = {
#     'phone': 'Disk',
#     'chair': 'floor',
#     'pen': 'notebook'
# }

# for key, value in where_my_things_are.items():
#     print(f"My {key} is kept on the {value}")

###################################

# colors = ['red', 'green', 'blue']

# colors.insert(2, 'yellow')

# for idx, color in enumerate(colors): # we have to include enumerate only if we want the index
#     print(idx, color)

###################################

# nums = [1,2,3,4,5,6,7,8,9,10]
# squares = [n*n for n in nums if (n*n)%2 == 0]
# print(squares)

###################################

# nums = (1,2,3) # if you want it to be a tuple you have to include a comma if it's one value because if not included it will read it as an int
# # nums = (1,) this will be tuple & nums = (1) will be an int
# print(type(nums))
# print(nums.index(1))

###################################

# # to slice we use this method
# name = ['a','b','c','d','e'][0:3] # it will only keep elements from 0 to 2 without including the third index
# print(name)

###################################

# fruit = {
#   'apples': 'red',
#   'bananas': 'yellow',
#   'oranges': 'orange'
# }

# color_of_bananas = fruit['bananas']
# print(color_of_bananas)

###################################

# one, two, three = 'abc'
# print(two) # we get b because strings have indexes