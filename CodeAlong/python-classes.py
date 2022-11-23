class Dog():
    next_id = 1
    # init is constructor in JS
    # self is 'this' in JS -> this.name
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1
    
    def bark(self):
        print(f"{self.name} says woof!")
    
    # overwriting the __str__
    def __str__(self):
        return (f"Dog {self.id} named {self.name} is {self.age} years old.")

spot = Dog('spot', 8)
fluff = Dog('fluff', 4)
# print(spot)
# print(dir(spot)) # directory
print(spot.name)
print(spot.age)
spot.bark()

print(spot) # this prints what's in the __str__
print(fluff)