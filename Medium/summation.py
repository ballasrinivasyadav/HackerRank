
# Digit summation

num = int(input("Enter numbers:"))
result = 0
while num>0:
    digit = num%10
    result = result+digit
    num = num//10
print("The sum of digits are:",result)


for i in range(len(str(num))):
    digit = num%10
    result = result+digit
    num = num//10
print("The sum of values are:",result)

# first loop
print(123%10)
print(123//10)
#second loop
print(12%10)
print(12//10)
#Third loop
print(1%10)
print(1//10)


