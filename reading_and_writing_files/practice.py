import csv

filename = 'invoices.csv'
data=[]
with open(filename, encoding='utf-8',newline='') as readfile:
    reader = csv.reader(readfile, delimiter ='\t')
    for row in reader:
        data.append(row)
print(data)

savefile = 'invoices2.csv'
with open(savefile,'w',encoding='utf-8',newline='') as writefile:
    writer = csv.writer(writefile,delimiter= '\t')
    writer.writerows(data)
