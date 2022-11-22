# Question1

def sum_to(num):
    return num * (num +1) // 2

print(sum_to(6))

# Question 2

def largest(ls):
    return max(ls) 
 
print(largest([1, 2, 3, 4, 0]))

# Question 3

def occurances(str1 , str2):
    return str1.count(str2)

print(occurances('fleep floop', 'oo')) # returns 1

# Question 4

import numpy as np
# using numpy.prod() to get the multiplications  
def product(*args):      
    return np.prod(args)  
print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0



