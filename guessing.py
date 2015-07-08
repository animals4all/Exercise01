import random

print "Welcome to the Number Guessing Game!"

name = raw_input("Please enter your name: ")
number = random.randint(1, 100)
highScore = 9999999999
turnNumber = 0

print "%s, try to guess the number I'm thinking of. It's between 1 and 100." % name
print ""

while True:
	try:
		guess = int(raw_input("Your guess?: "))
		if guess < 1 or guess > 100:
			print ""
			print "Your guess must be a number between 1 and 100."
			print ""

		else:
			turnNumber += 1
			if guess < number:
				print ""
				print "Your guess is too low."
				print ""
			elif guess > number:
				print ""
				print "Your guess is too high."
				print ""
			else:
				print ""
				print "Congratulations, %s! You correctly guessed my number." % name
				print ""
				if turnNumber < highScore:
					highScore = turnNumber
					print "New record: %d" % highScore
					print ""
				turnNumber = 0

				if raw_input("Want to play again?: ").lower() in ("y", "yes"):
					print ""
					number = random.randint(1, 100)
					print "%s, try to guess the number I'm thinking of. It's between 1 and 100." % name
					print ""
				else:
					break

	except ValueError:
		print ""
		print "That's not a number!"
		print ""