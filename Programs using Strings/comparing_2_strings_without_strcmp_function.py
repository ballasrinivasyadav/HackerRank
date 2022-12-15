
# comparing 2 strings without strcmp function

str1 = input("Enter Elements:")
str2 = input("Enter Elements:")
lstr1 = len(str1)
lstr2 = len(str2)

if lstr1 == lstr2:
   n = 0
   k = 0
   while n<lstr1:

       if str1[n] != str2[n]:
           k =1
           break
       n = n+1
   if k == 0:
       print("\n Strings are equal")
   else:
       print("\n Strings are not equal")
else:
    print("\n Strings are not equal")
