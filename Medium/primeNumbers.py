# Prime numbers between two ranges

#
# num = int(input("Enter prime numbers:"))
#
# if num>1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             print(num," Not Prime numbers")
#             break
#     else:
#         print(num,"prime numbers")
# else:
#     print(num,"Not prime numbers")
#

lower = 2
upper = 10

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)