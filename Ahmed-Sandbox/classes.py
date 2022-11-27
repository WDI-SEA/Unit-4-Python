# nums = [1,2,3,4,5,6,7,8,9,10]

# print(dir(nums))


class Dog():

    # class attribute
    next_id = 1

    # is like the constructor function in JS
    # self in Python == this in JS
    # age = 0 is default value
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1
    
    def bark(self):
        print(f"{self.name} says woof!")

        
    # Override the str method so when we print rocky it will be
    # this string name instead of memory
    def __str__(self):
        return f"Dog Name is {self.name} and the age is {self.age}"
    

    # use it only on the class not on an instance
    # Dog.get_total_dogs() will work
    # But Rocky = Dog()
    # Rocky.get_total_dogs() will NOT work

    @classmethod
    def get_total_dogs(cls):
        return cls.next_id -1

# No need for new keyword
rocky = Dog('Rocky', 5)
print(rocky.id)


# No need for new keyword
fluffy = Dog('Fluffy', 5)
print(fluffy.id)


print('Dog Numbers', Dog.get_total_dogs())


# Inheritance

class ShowDog(Dog):

  # Add additional parameters AFTER those in the superclass
    def __init__(self, name, age = 0, total_earnings = 0):
        # Always call the superclass's __init__ first
        Dog.__init__(self, name, age)
        # Now add any new attributes
        self.total_earnings = total_earnings

    def add_prize_money(self, amount):
        self.total_earnings +=amount

winky = ShowDog('Winky', 3, 1000)
print(winky) # Yay, inherited the overriden __str__
winky.bark() # Yay, inherited the bark method
print(winky.total_earnings) # -> 1000
winky.add_prize_money(500) # New method that 'Dogs' don't have
print(winky.total_earnings) # -> 1500