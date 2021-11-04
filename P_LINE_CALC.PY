fin = open('REPORT/test.txt', 'r')
fout = open('REPORT/plines.txt', 'a')
s = fin.readlines()
for j in s:
    if 'p' in j:
        fout.write(j)
fin.close()
fout.close()
