
# Convert the file contents in Upper-case & Write Contents in a output file

fname = open('a.txt','r')
for x in fname.read():
    y = x.upper()
    f1 = open('b.txt','a')
    fname.write(y)

