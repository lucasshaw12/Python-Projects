#! python3
# Find all filenames with a specified extension. If the sequence has gaps, fill them in with new files.
# e.g. # Locate any gaps in the numbering such as (Txt2.txt and Txt0.txt - but no Txt1.txt) 
import os, re, shutil
from pathlib import Path

# Create a folder within the current working directory
os.makedirs('Txt Files', exist_ok=True)
absWorkingDir = os.path.abspath('.') 

# Populate folder with .txt files, deliberately skipping every other filename number (0, 2, 4, 6, 8)
for newFile in range(0, 10, 2): 
	newFile = open(f'{absWorkingDir}/Txt Files/Txt{newFile}.txt', 'w')

# Find all files in a single folder with a given prefix of .txt
txtFolder = Path(f'{absWorkingDir}/Txt Files/')
fileNumber = 1
for txtFile in os.listdir(txtFolder):
	if txtFile.endswith('.txt'):

		# Create a regular expression to find the files
		fileNamePattern = re.compile(r'(^Txt)(\d+)')
		mo = fileNamePattern.search(txtFile)

		newFilename = 'new' + mo.group(1) + str(fileNumber) + '.txt'
		fileNumber += 1

		cwd = os.path.abspath(txtFolder)
		oldPath = os.path.join(cwd, txtFile)
		newPath = os.path.join(cwd, newFilename)
		print(oldPath)
		print(newPath)
		
		shutil.move(oldPath, newPath)




