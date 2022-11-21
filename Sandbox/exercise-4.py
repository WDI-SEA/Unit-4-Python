a = input("a: ")
b = input("c: ")
c = input("c: ")

triangle_type = ""

if a == b and b == c and c == a:
    triangle_type = "equalateral"
elif a != b and b != c and c != a:
    triangle_type = "scalene"
elif a == b or b == c or c == a:
    triangle_type = "isosceles"

print(f"A triangle with sides of {a}, {b} & {c} is a {triangle_type} triangle")