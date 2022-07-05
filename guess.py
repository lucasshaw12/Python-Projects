import random
import sys

print('I am thinking of a number between 1 and 20')

number = random.randint(1, 20)

print(number)

for guessesTaken in range(1, 10):
	guess = int(input())
	if guess < number:
		print('Too low, try again')
	elif guess > number:
		print('Too high, try again')
	else:
	   break

if guess == number:
	print('Well done, you got it right in {} attempts'.format(guessesTaken)) #first way of printing the text
	print('Well done, you got it right in ' + str(guessesTaken) + ' attempts') #second way of writing the text
else:
	print('Incorrect, you didnt get it this time!') 








