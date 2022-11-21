letter = " "
while letter != "quit":
    letter = input('Please enter a letter from the alphabet (a-z or A-Z): ')
    
    if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is not a vowel")