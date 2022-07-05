#! python3
# A multiplication quiz
import pyinputplus as pyip
import time, random

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
	num1 = random.randint(0,9)
	num2 = random.randint(0,9)

	prompt = '%s: %s x %s = ' % (question_number, num1, num2)

	try:
		# Correct answers are handled by allowRegex
		# Incorrect answers are handled by blockRegex, with a custom message
		pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
			blockRegexes=[('*.', 'Incorrect')],
			timeout=8, limit=3
			)
	except pyip.TimeoutException:
		print('Out of time')
	except pyip.RetryLimitException:
		print('Out of tries')
	else:
		# This else raises when there are no errors caught by the above 'except'
		print('Correct')
		correct_answers += 1

	time.sleep(1) # Brief pause to allow the user to read to the score
	print('Score: %s / %s' % (correct_answers, number_of_questions))
