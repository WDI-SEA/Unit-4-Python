print("Enter the lengths of three side of a triangle:")
a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))

if(a == b == c):
    print("The triangle is equalateral")
elif(a == b or a == c or b == c):
    print("The triangle is isosceles")
else: 
    print("The triangle is scalene")