import csv
file = open('research-and-development-survey-2019-csv.csv')

file_reader = csv.reader(file)
for row in file_reader:
    print('Row no'+' '+str(file_reader.line_num)+' '+str(row))