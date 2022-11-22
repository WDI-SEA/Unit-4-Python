#3

years = " "
while years != "quit":
    years = input("Input a dog's age in human years: ")
    human_years = int(years)
    
    if human_years < 0:
    	print("Age must be positive number.")
    	exit()
    elif human_years <= 2:
	    dog_years = human_years * 10
    else:
	    dog_years = 20 + (human_years - 2)*7
    
    print(f"The dog's age in dog years is {dog_years}")