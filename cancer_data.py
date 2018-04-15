import xlsxwriter
data = open('mutation_1.tsv','r')
data2 = open('mutation_2.tsv','r')
mutation = {}
indel_count = 0
for line in data:
    line = line.strip("\n")
    if 'del' in line or 'ins' in line:
        indel_count += 1
    for i in range(len(line)):
        if line[i] == '>':
            if line[i-1:] in mutation:
                mutation[line[i-1:]] += 1
            else:
                mutation[line[i-1:]] = 1
        continue

for line in data2:
    line = line.strip("\n")
    if 'del' in line or 'ins' in line:
        indel_count += 1
    for i in range(len(line)):
        if line[i] == '>':
            if line[i-1:] in mutation:
                mutation[line[i-1:]] += 1
            else:
                mutation[line[i-1:]] = 1
        continue

mutation['indel'] = indel_count
print(mutation)
data.close()
data2.close()

workbook = xlsxwriter.Workbook('datalel2.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for key in mutation.keys():

    worksheet.write(row,col,key)
    worksheet.write(row,col+1, mutation[key])
    row += 1

workbook.close()