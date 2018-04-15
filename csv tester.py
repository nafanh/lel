import pandas as pd
import xlsxwriter

colnames = ['Reference','Alternate']
data = pd.read_csv('exac.csv', usecols=colnames)
col_reference = list(data.Reference)
col_alternate = list(data.Alternate)
combined = {}
for i in range(len(col_reference)):
    trans = col_reference[i] + ' -> ' + col_alternate[i]
    if trans in combined:
        combined[trans] += 1
    else:
        combined[trans] = 1

combined_percentages = {}
for mutation in combined:
    combined_percentages[mutation] = round((100*(combined[mutation]/sum(combined.values()))),2)
print(combined_percentages)

workbook = xlsxwriter.Workbook('datalel.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for key in combined_percentages.keys():

    worksheet.write(row,col,key)
    worksheet.write(row,col+1, combined_percentages[key])
    row += 1

workbook.close()
