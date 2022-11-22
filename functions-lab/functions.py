# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(6))




# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231



def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

def largest(nums):
  nums.sort()
  return nums[-1]

print(largest([1, 2, 3, 4, 0]))




# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0


# def occurances(string, substr):

#   stripped_string = string.replace(substr, '')

#   return (len(string) - len(stripped_string)) // len(substr)


# def occurances(string, substr):
#   return string.count(substr)

message = ('fleep floop')

print(message.count('fl'))




# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# For example:

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0



def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(2,5,5))


