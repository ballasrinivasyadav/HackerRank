
# Copy from one text file into another

with open('a.txt','r') as f1 ,open('b.txt','w') as f2:

    for line in f1:
        f2.write(line)


