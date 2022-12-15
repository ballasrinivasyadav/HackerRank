# Length of a string using pointers
# Basic Level Coding
str1 = 'Python Programming Language'
s = len(str1)
print(s)

# Intermediate Level Coding
count = 0
for i in range(len(str1)):
    if i >= count:
        count += 1
print("Length of a string using Language:", count)

# Medium Level Coding
def length_num(str2, count):
    for i in range(len(str2)):
        if i >= count:
            count += 1
    print("Length of a string using Language:", count)

count = 0
str2 = 'Python is a dynamically typed language program'
length_num(str2, count)

# Class Level Program
class LangthNum():
    def length_num(self,str3,count):
        for i in range(len(str3)):
            if i >= count:
                count += 1
        print("Length of a string using Language:", count)

    count = 0
    str3 = 'Python is a dynamically typed language programs'

LangthNum()
