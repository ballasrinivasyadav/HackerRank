
fname = input("Enter filename:")
k = 0

with open(fname,'r') as f:
    for line in f:
        words = line.split()
        for letters in words:
            if(letters.isspace):
                k = k+1
print("Occurances of black spaces:")
print(k)
print(letters)
print(words)