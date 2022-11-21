side_1 = int(input('Enter the lengths of three side of a triangle: \na:' ))
side_2 = int(input('b:' ))
side_3 = int(input('c:' ))

if side_1 == side_2 and side_1 == side_3:
    print(f"A triangle with sides of a:{side_1} , b:{side_2} , c:{side_3} is a type of equalateral triangle")
elif side_1 == side_2 :
    print(f"A triangle with sides of a:{side_1} , b:{side_2} , c:{side_3} is a type of isosceles triangle")
elif side_1 == side_3 :
    print(f"A triangle with sides of a:{side_1} , b:{side_2} , c:{side_3} is a type of isosceles triangle")
elif side_2 == side_3:
    print(f"A triangle with sides of a:{side_1} , b:{side_2} , c:{side_3} is a type of isosceles triangle")
else:
    print(f"A triangle with sides of a:{side_1} , b:{side_2} , c:{side_3} is a type of scalene triangle")