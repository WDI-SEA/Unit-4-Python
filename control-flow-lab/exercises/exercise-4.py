print("Enter the lengths of three side of a triangle: ")
a = input("a: ")
b = input("b: ")
c = input("c: ")

if(a==b and b==c and a==c):
    print("equalateral - all three sides are equal in length")
elif(a==b or b==c or a==c):
    print("isosceles -  two sides are the same length")
else:
    print("scalene - all three sides are unequal in length")