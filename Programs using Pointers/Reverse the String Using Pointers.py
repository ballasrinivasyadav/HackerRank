
# Reverse the String Using Pointers
s = 'python'
count = s[::-1]
for i in range(len(count)):
    if i == s[::-1]:
        count+=1
print(count)
# Reversed
for i in reversed(s):
    print(i,end='')
print('\n')
##########
#s = p y t h o n
#    0 1 2 3 4 5
s1 = ''
le = 5
s1 = s1+s[le]
print(s1)
##########
def len_Num(s2,s3,length):

    while length >= 0:
        s3 = s3+s2[length]
        length = length-1
    print(s3)
s2 = 'Program'
s3 = ''
length = len(s2)-1

len_Num(s2,s3,length,)

############
