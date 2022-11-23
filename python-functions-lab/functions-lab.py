def to_sum(n):
    sum = 0
    for num in range(1,n+1):
        sum+=num
    return sum
        
def largest(list):
    print(max(list))

def occurances(word, seekedItem):
    return word.find(seekedItem)


def product(*args):
    result =1
    for n in args:
        result*=n
    return result

print(product(2,2))