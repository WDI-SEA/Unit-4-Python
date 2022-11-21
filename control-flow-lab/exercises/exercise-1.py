alphabet = input("Please enter a letter from the alphabet (a-z or A-Z): ")

vowls = ["a", "e", "i", "o", "u"]

if(alphabet in vowls):
    print(f"The letter {alphabet} is a vowel")
else:
    print(f"The letter {alphabet} is a consonant")