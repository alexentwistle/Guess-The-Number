import random

result = random.randint(1,5)

guess = int(input("Guess the number:"))


while True:	
	if guess < result:
		print("Too low.")
		break
	elif guess > result: 
		print("Too high.")
		break
	else: 
		print("Well done!")
		break


# TODO - add guess again option
