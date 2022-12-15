
# Count number of words using pointers

s = len('python programming language'.split())
print(s)

g = 'python','progamming','language'
count = 0
for i in range(len(g)):
    if i >= count:
        count += 1
print("Number of word are in sentences:",count)




def number_count(g,count):
    for i in range(len(g)):
        if i >= count:
            count += 1

    print("Number of words counting in sentences using pointers are  :", count)
count = 0
g = 'python','progamming','language'
number_count(g,count)



