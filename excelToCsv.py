#! python3
# Read all excel files in the current directory and convert them to .csv files
# Create a CSV file per excel 'sheet'

import os
import pandas as pd  

# Create a new folder for .csv files 
os.makedirs('./excelToCSV/', exist_ok=True) 
CSVFolder = './excelToCSV/' 

for excelFile in os.listdir('./excelspreadsheets'): 
    if excelFile.endswith('.xlsx'): # Skip non xlsx files, load the workbook object 
        xls = pd.ExcelFile('./excelspreadsheets/' + excelFile) # Read the excel files 
        for sheetname in xls.sheet_names: 

            # Read each sheet into df 
            df = pd.read_excel('./excelspreadsheets/' + excelFile, sheetname) 

            # Remove .xlsx from filename and create CSV name 
            CsvFilename = excelFile.rstrip('.xlsx') + '_' + sheetname + '.csv' 
            print(f'Creating filename {CsvFilename}...') 

            # Write df as CSV to file 
            df.to_csv(CSVFolder + CsvFilename, index=False) 

 