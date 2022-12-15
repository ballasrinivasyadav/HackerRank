
# Count the number of digit in an integer

n = int(input("Enter numbers:"))
count = 0
while n>0:          # 2 True
    count=count+1  # 0=0+1 == 1

    n = n//10  # 12=12//10 = 1
             # 1 = 1//10 = 0
             # 100 = 111//10 == 10

    # ANS: count= 1 + n = 1 = 2
    #               1 +  0  = 1
    #               1 +  11 = 3
print("numbers",count)

