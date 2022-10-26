# Reading .csv-data and storing it in an .xls-file
# We use the built-in Python csv-module for that.

# 0. Import stuff we need
import csv
from openpyxl import Workbook

# 1. Create a workbook and grab the active sheet
wb = Workbook()
ws = wb.active

# 2. Instructions for the user
print('Reading csv-data from a textfile and storing it in an Excel-sheet.')
fileName = input('What file do you want to open? (must be CSV-format)')

# 3. Open the file and work with it
try:
    with open(fileName, mode='rt', encoding='utf-8') as file:
        # 4. Create Reader object from the csv-file. 
        # In this case we use for instance <keyword>.prices.txt file that 
        # was generated from workshop-30.py.
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(row)
            ws.append(row)
except Exception as ex:
    print('Error!', ex)

# 5. Save the Excel-file and inform user
excelFile = '{0}.xlsx'.format(fileName)

wb.save(excelFile)
print('Done! Saved as {0}'.format(excelFile))