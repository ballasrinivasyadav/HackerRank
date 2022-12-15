
# Find largest among three numbers

num = 10
num2 = 15
num3 = 20

if (num >= num2) and (num >= num3):
    largest = num
elif (num2 >= num) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number:",largest)