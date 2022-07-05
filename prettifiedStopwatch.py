#! python3
# A stopwatch program that has been formatted using pprint

import time, datetime, pyperclip
# Display the programs instructions
print('Press "ENTER" to begin. Press "ENTER" to click the stopwatch. Press "Ctrl-C" to quit')
input()
print('Started.')

startTime = datetime.datetime.now()
lastTime = startTime
lapNum = 1

# Track the lap times
try:
	while True:
		input()
		lapTime = datetime.datetime.now() - lastTime
		totalTime = datetime.datetime.now() - startTime
		# lapTime.strftime('%H:%M:%S')
		# totalTime.strftime('%H:%M:%S')

		lapTimeStr = str(lapTime.total_seconds())
		totalTimeStr = str(totalTime.total_seconds())

		lapNumStr = str(lapNum)
		print('Lap #%s: %s (%s)' % (lapNumStr.ljust(2), totalTimeStr[0:4].center(10), lapTimeStr[0:4].ljust(3)), end='')
		lapNum += 1
		lastTime = datetime.datetime.now() # reset the last lap time
		copiedText = 'Lap #%s: %s (%s)' % (lapNumStr.ljust(2), totalTimeStr.center(10), lapTimeStr.ljust(3))
		pyperclip.copy(copiedText)


except KeyboardInterrupt:
	# Handle the Ctrl-C exeptions to keep its error message from displaying.
	print('\nDone.')
