#! python3
# Probabilities of the coin flip results landing 6 consecutive 'heads' or 'tails'.

import random
numberOfStreak = 0
flip = []
streak = 0

for experimentNumber in range(100):
	# creates a 10,000 turn 'for' loop
	for i in range(100):
		flip.append(random.randint(0, 1))

	for i in range(len(flip)):	
		if i == 0:
			pass
		elif flip[i] == flip[i-1]:
			streak += 1
		else:
			streak = 0

		if streak == 6:
			numberOfStreak += 1	

print('\nChance of streak: %s%%' % (numberOfStreak / 100))