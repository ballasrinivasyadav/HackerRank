# Number palindrome

# string = input("Enter Letter:")
#
# if (string==string[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


number = int(input("Enter numbers:"))
num = str(number)
rev_num = num[::-1]
if num == rev_num:
    print("Palindrome")
else:
    print("Not Palindrome")


# n = int(input("Enter number:"))
# temp = n
# rev = 0
#
# while(n > 0):
#
#     dig = n % 10
#     rev = rev*10+dig
#     n = n//10
# if(temp==rev):
#
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")