f = open("REPORT/test.txt", "r")
count = 0
print(f.read())
f.seek(0)
for line in f:
    words = line.split()
    count = count+len(words)
print("No of words present in string are:", count)
