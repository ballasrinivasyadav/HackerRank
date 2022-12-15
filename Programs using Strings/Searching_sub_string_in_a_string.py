
# Searching sub string in a string

s = ['ss','dd','rr','gg']
print(s[::-1])
g = " ".join(s)
print(g)
print(s[0])

str1 = "Geeks for geeks"
if "geeks" in str1:
    print("Yes")
else:
    print("No")

#Spitting method
substring1 = "geeks"
s = str1.split()
if substring1 in str1:
    print("Yes")
else:
    print("No")

#Count
def count1(str1,substring):
    if (str1.count(substring)>0):
        print("string is there")
    else:
        print("string is not there")
str1 = "geeks for geeks"
substring1 = "geeks"
count1(str1,substring1)