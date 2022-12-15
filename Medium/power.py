
# Calculate x to the power y

def power(x,y):
    return x**y
print(power(2,2))


base = 4
exponent = 2
result = 1

for exponent in range(exponent):
    result*=base
print("Answer = ",result)