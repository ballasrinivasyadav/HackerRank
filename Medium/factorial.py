
# Factorial without using function

n = int(input("Enter numbers:"))
fact = 1
if n<0:
    print("Factorial doesn't exit for negative numbers")
else:
    for i in range(1,n+1): # 1,4 = 1,2 = (1*1=1)*(1*2=2)  == 2
                           # (2*3=6) == 6
                           # (6*4) == 24

        fact = fact*i
    print("factorial of ",n,"is",fact)
