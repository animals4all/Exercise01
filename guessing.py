import random

print "Welcome to the Number Guessing Game!"

name = raw_input("Please enter your name: ")
number = random.randint(1, 100)

print "%s, try to guess the number I'm thinking of. It's between 1 and 100." % name
print ""

while True:
	guess = int(raw_input("Your guess?: "))
	if guess < number:
		print ""
		print "Your guess is too low."
		print ""
	elif guess > number:
		print ""
		print "Your guess is too high."
		print ""
	else:
		print "Congratulations, %s! You correctly guessed my number. It was %d." % (name, number)
		break
