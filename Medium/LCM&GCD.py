# LCM

def compute_lcm(x,y):
    if x>y:
        greater = x   # 10
    else:
        greater = y    # 8
    value = greater   # 10
    while True:
        if greater % x == 0 and greater % y == 0:

             #10 % 10  == 0 and 10 % 8 ==0
            print("LCM of",x,"and",y,"is",greater)
            break
        else:
            greater = greater + value







print("LCM:",compute_lcm(10,8))

# Greater Common Divisor

def compute_gcd(x,y):

    if x>y:
        small = x
    else:
        small = y

    for i in range(1,small+1):
        if ((x % i == 0 and y % i == 0)):
            gcd = i
    return gcd

# Expected Output

print("GCD:",compute_gcd(10,8))