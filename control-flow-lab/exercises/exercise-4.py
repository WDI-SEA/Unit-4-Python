# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

side_1 = int(input('Enter the lengths of three side of a triangle: \na:' ))
side_2 = int(input('b:' ))
side_3 = int(input('c:' ))

type_of_triangle = ""

if side_1 == side_2 and side_1 == side_3:
    type_of_triangle = "equalateral"
elif side_1 != side_2 and side_2 != side_3 and side_3 != side_1 :
    type_of_triangle = "scalene"
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    type_of_triangle = "isosceles"
    
print(f"A triangle with sides of a:{side_1}, b:{side_2} & c:{side_3} is a {type_of_triangle} triangle")
