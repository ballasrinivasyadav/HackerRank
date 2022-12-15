
# Fibonacci starting from any two numbers

n = int(input("Enter number:"))
first = 0
second = 1

for i in range(n):
    print(first,end=" ")
    temp = first
    first = second
    second = first+temp

count = 0
while count < n:
    print(first)
    temp = first
    first = second
    second = first + temp
    count += 1

