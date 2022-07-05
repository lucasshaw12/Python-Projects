#! python3
# Download Google Sheets form data and display all the email addresses

import ezsheets
# Access the spreadsheet
ss = ezsheets.Spreadsheet('Python test responses')
sheet = ss[0]
columns = sheet.getColumn(2)
rows = sheet.getRows()

# Trim the list. Then use the list to count the number of responses
numOfResponses = []
for col in columns:
	if col != '':
		numOfResponses.append(col)

numOfQuestions = []
for row in rows[1:]: # Ignore the first row
	if row != '':
		numOfQuestions.append(row)

rowLen = len(numOfResponses) # Set the amount of rows respective to the responses received
sheet.rowCount = rowLen

colLen = len(numOfQuestions) # Set the amount of columns respective to the questions asked
sheet.columnCount = colLen

emailAddresses = sheet.getColumn(3) # Get the column that contains the email addresses
for i, value in enumerate(emailAddresses[1:]): # Again, ignore the first row
	print(i, value)