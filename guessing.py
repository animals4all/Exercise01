import random

print "Welcome to the Number Guessing Game!"

name = raw_input("Please enter your name: ")
number = random.randint(1, 100)

print "%s, try to guess the number I'm thinking of. It's between 1 and 100." % name
print ""

while True:
	guess = int(raw_input("Your guess?: "))