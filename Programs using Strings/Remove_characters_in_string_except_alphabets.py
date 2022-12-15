
# Remove characters in string except alphabets
str1 = "Python!77@gmail.com"

get_list = list([i for i in str1 if i.isalnum() and i.isalpha()])
print(get_list)
result = "".join(get_list)
print(result)