
# convert a name into its ascii values.

test_list = ['gfg','is','best']

print("Original list: " + str(test_list))

res = []
for ele in test_list:

    res.extend(ord(num) for num in ele)

    # res.extend(ord(num) for num in ele)

print("Result of ascii list is :"+str(res))
