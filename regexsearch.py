#! python3
# Search for a string of text within all .txt files. Return the files and strings which contain that text

from pathlib import Path
import re
import os

# open up all .txt files within /Users/Lucas
findDir = Path('/Users/Lucas/')

searchedWord = input('\nEnter the word that you wish to find: ')

# loop through the generator that glob returns
for txtFiles in findDir.glob('*.txt'):
	openFile = open(txtFiles)
	readTxtFiles = openFile.read()
	fileName = os.path.basename(txtFiles)

	# use the input as a regex expression to find sample
	regex = re.compile(searchedWord)
	txtRegex = regex.findall(readTxtFiles)

	if not txtRegex:
		pass
	else:	
		print(f'These files have the string "{searchedWord}": "{fileName}"')


	
