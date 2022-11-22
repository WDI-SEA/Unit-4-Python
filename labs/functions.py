# 1
def sum_to(n):
    total = n * (n + 1) // 2
    print(f"The sum of the integers from 1 to {n} is {total}")

sum_to(6)
sum_to(10)

# 2
def largest(list):
    largest_num = max(list)
    print(f"Largest number is {largest_num}")

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

# 3
# def occurances(string, substr):
#   # remove each occuance of substr
#   stripped_string = string.replace(substr, '')
#   # compute based on length of the strings
#   return (len(string) - len(stripped_string)) // len(substr)

# Python actually has a method to solve this too!
def occurances(string, substr):
  return print(string.count(substr))

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0

# 4
def product(*args):
    multiply = 1
    for m in args:
        multiply *= m
    return (print(f"Product of given numbers is {multiply}"))

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0