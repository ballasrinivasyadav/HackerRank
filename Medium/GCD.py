# Greater Common Divisor
def computeGCD(x,y):
    if y == 0:
        return x
    else:
        return computeGCD(y,x%y)
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print(computeGCD(x,y))

# Ex:1
# x = 64     y = 48
# 64 = 48 x X + remainder (x%y)
# 64 = 48 x 1 + 16
# 48 = 16x3 + 0
# 16 = 0
# x    y
# or
# 16 [64,48]
    # 4,3

# Ex:2

# x = 18   y=4
# 18 = 4 x X + remainder (x%y)
# 18 = 4 x 4 + 2
# 4 = 2 x 2 + 0
# 2 = 0
# x   y

