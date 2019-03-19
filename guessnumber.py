import random

result = random.randint(1,5)

guess = int(input("Hi. I'm thinking of a number between 1 and 5. Guess the number:"))

while result != guess:
	if guess < result:
		print("Too low. Guess again?")
		guess = int(input("Enter a number between 1 and 5:\n"))
	elif guess > result: 
		print("Too high. Guess again?")
		guess = int(input("Enter a number between 1 and 5:\n"))
	else: 
		break

print("Well done! The number was %d." % result)
