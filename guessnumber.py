import random

result = random.randint(1,100)

guess = int(input("Hi. I'm thinking of a number between 1 and 100. Guess the number:"))

while result != guess:
	if guess < result:
		print("Too low! Guess again?")
		guess = int(input("Enter a number between 1 and 100:\n"))
	elif guess > result:
		print("Too high! Guess again?")
		guess = int(input("Enter a number between 1 and 100:\n"))
	else: 
		break

print("Well done!!! The number was %d." % result)

#TODO: Print number of guesses the user took.