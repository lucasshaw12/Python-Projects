#! python3
# A rock, paper, scissors game.

import sys
import random

wins = 0
losses = 0
ties = 0
turn = 0

rps = ['Rock', 'Paper', 'Scissors']
choice = random.choice(rps)
print(choice)


while True:  # Main game loop
	print('\n{} wins, {} losses, {} ties'.format(wins, losses, ties))  # first way of writing the text
	print(str(wins) + ' wins ' + str(losses) + ' losses ' + str(ties) + ' ties')  # second way of writing the text
	print('\n')

	while True:
		playerMove = input('Enter your playerMove: (r)ock, (p)aper (s)cissors or (q)uit:'.capitalize())
		if playerMove == 'q':
			sys.exit(0)
		if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
			turn = turn + 1
			print('\nTURN: ' + str(turn))	
			break
		print('Type one of r, s, p, or q')

	# print the players guess	
	if playerMove == 'r':
		print('ROCK vs... ')
	elif playerMove == 'p':
		print('PAPER versus...')
	elif playerMove == 's':	
		print('SCISSORS versus...')

	# print the comps guess
	randomNum = random.randint(1, 3)
	if randomNum == 1:
		compMove = 'r'
		print('ROCK')
	if randomNum == 2:
		compMove = 'p'
		print('PAPER')	
	if randomNum == 3:
		compMove = 's'
		print('SCISSORS')

	# display and record the wins/losses/ties

		# Tie
	if playerMove == compMove:
		print("It's a tie")
		ties = ties + 1

		# Win
	if playerMove == 'r' and compMove == 's':
		print('You win!')
		wins = wins + 1
	if playerMove == 's' and compMove == 'p':
		print('You win!')
		wins = wins + 1
	if playerMove == 'p' and compMove == 'r':
		print('You win!')
		wins = wins + 1		

		# Loss
	if playerMove == 'r' and compMove == 'p':
		print('You lose!')
		losses = losses + 1
	if playerMove == 'p' and compMove == 's':
		print('You lose!')
		losses = losses + 1
	if playerMove == 's' and compMove == 'r':
		print('You lose!')
		losses = losses + 1
