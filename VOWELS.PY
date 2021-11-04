f = open("myfile.txt", "w")
f.write("Counting the number of vowels in this sentence")
f.close()
f = open("myfile.txt", "r")
t = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print(f.read())
f.seek(0)
for i in f.read():
    if i in vowels:
        t = t+1
f.close()
print("Total vowels are:", t)
