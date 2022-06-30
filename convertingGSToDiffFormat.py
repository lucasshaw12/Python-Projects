#! python3
# NOTE: Personal Google API and Auth credentials.json is required for this script to work
# Create a spreadsheet
# Upload a sheet to Googlesheets
# Download the sheet into excel and ODS
# Create copies of the spreadsheets

import ezsheets
import openpyxl

# Create a save a .xlsx workbook
wb = openpyxl.Workbook()
wb.save('testsheet.xlsx')

# Upload the workbook
uploadSS = ezsheets.upload('testsheet.xlsx')
ss = ezsheets.Spreadsheet('testsheet')

# Add some content to the spreadsheet
ss[0].updateRow(1, ['This', 'is', 'test', 'text'])

# Download the spreadsheet from GooglsSheets
ss.downloadAsExcel('downloadAsExcel-CAN-BE-DELETED')
ss.downloadAsODS('downloadAsOpenoffice-CAN-BE-DELETED')
ss.downloadAsPDF('downloadAsPDF-CAN-BE-DELETED')

# Delete the uploaded spreadsheet
ss.delete('testsheet')
