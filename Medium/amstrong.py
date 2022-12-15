# Amstrong checking

# Ex1: 371
print(3**3+7**3+1**3)

num = int(input("Enter numbers:"))
for i in range(num):
    num = i
    result = 0
    n = len(str(i))
    while (i!=0):
        digit = i%10
        result = result+digit**n
        i=i//10
    if num == result:
        print(num)

print(100%10)
print(100//10)

