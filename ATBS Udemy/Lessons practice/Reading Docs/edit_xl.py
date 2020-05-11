import openpyxl
import os
wb = openpyxl.Workbook()
print(wb)

print(wb.sheetnames)

sheet = wb['Sheet']
print(sheet)
print(sheet['A1'].value)
print(sheet['A1'].value == None)


sheet['A1'] = 'Name'
sheet['B1'] = 'Marks'
os.chdir('C:\\Users\\rahul.goyal\\Documents')
wb.save('marks.xlsx')