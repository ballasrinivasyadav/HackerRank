
# Copying the content of one file into another

with open('a.txt') as f:
    with open('b.txt','w') as f1:
        for line in f:
            f1.write(line)
print(line)