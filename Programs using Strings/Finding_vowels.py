# Finding vowels
#(1) for counting purpose
str1 = 'string'
count = 0
for i in str1:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count = count+1
print(count)

#(2) For finding vowels in string
str2 ='strings are vowels'
m = []
for i in str2:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        m.append(i)
l=" ".join(m)
print(l)

#(3) For counting & finding vowels in string
str3 ='strings are vowels'
k = []
count = 0
for i in str3:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        k.append(i)
        count += 1
l=" ".join(k)
print(l)
print(count)

#(4) Vowels in string print in list format
str4 = 'you have to check vowels in strings'
o = []
for i in str4:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        o.append(i)
print(o,end='')

# Print Vowels in function format
str5 = 'you have to check vowels in strings'
g = []
count = 0
def vow(str5,count):
    for i in str5:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count = count+1
            g.append(i)
    print('\n')
    print(o)
    print(count)
(vow(str5,count))

