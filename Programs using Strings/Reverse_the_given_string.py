# Reverse the given string
str1 = 'string'
print(str1[::-1])


# Recursive Reverse String
def rev_str(str1):
    return str1[::-1]


print(rev_str(str1))

# For loop Method
rev_str1 = []
rev = reversed(str1)
for i in rev:
    rev_str1.append(i)
l = "".join(rev_str1)
print(l)

# While loop Method
str2 = 'python'
rev_str2 = ''
count = len(str2)
while count > 0:
    rev_str2 += str2[count - 1]
    count -= 1
print(rev_str2)

#################
# For loop Method with no string output
str3 = 'python'
rev_str = []
for i in str3:
    rev_str.append(i)
j = ''.join(rev_str)
revers = j[::-1]
print(revers)

# Another way of for loop printing in list format with strings
str4 = 'program'
lst = []
for j in str4:
    lst.append(j)
rev_lst = lst[::-1]
print(rev_lst)
