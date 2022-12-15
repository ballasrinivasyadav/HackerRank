
# Palindrome checking
my_string = input('Enter name:')
if my_string =='tet':
    print("Palindrome")
else:
    print("Not palindrome")

rev_string = reversed(my_string)

if list(my_string) == list(rev_string):
    print("Palindrome")
else:
    print("Not Palindrome")

