import csv
record = [['a', 10, 70], ['b', 12, 80], ['c', 14, 90]]
f = open('CSV_File.csv', 'w', newline='')
obj = csv.writer(f)
for i in record:
    obj.writerow(i)
print("Writing CSV file Complete")
f.close()
f = open('CSV_File.csv', 'r', newline='')
obj1 = csv.reader(f)
for row in obj1:
    print(row)
print("Reading Csv file Complete")
f.close()
