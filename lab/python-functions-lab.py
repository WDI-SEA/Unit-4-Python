#1
def sum_to (n):
  return n*(n+1)//2

print(sum_to(10))


#2
def largest(num):
    return max(num)

print(largest([1, 2, 3, 4, 0]))


#3
def occurances(string1, string2):
    count =0
    for word in string1:
        for character in word:
            if character == string2:
             count = count +1
    
    return count

first_str = input("Enter your word: ")
second_str = input (" Enter your word 2: ")
r_occurances = occurances(first_str, second_str)
print("There is ",r_occurances, second_str, "in", first_str)
  

#4
def product(*args):
    num = 1
    for item in args:
       num *= item
    return num


print(product(2, 5, 5))
