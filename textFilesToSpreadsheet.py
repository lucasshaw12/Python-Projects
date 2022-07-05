#! python3
# Read contents of several text files
# Insert lines of text into a spreadsheet
# First text file, column A etc...

from pathlib import Path
import openpyxl
listOfText = []

wb = openpyxl.Workbook() # Create a new workbook to insert the text files
sheet = wb.active

for txtFile in range(5): # create 5 text files
	createTextFile = Path('textFile' + str(txtFile) + '.txt')
	createTextFile.write_text(f'''Hello, this is a multiple line text file.
My Name is x.
This is text file {txtFile}.''')

	readTxtFile = open(createTextFile)
	listOfText.append(readTxtFile.readlines()) # nest the list from each text file into a parent list

textFileList = len(listOfText[txtFile]) # get the number of lines of text from the file. They are all 3 as made above

# Each column displays text from each text file
for row in range(1, txtFile + 1):
	for col in range(1, textFileList + 1):
		sheet.cell(row=col, column=row).value = listOfText[row-1][col-1]

wb.save('importedTextFiles.xlsx') # Save the workbook