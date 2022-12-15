
my_array = [1,2,3,4,5]
empty_lst = []
for i in my_array:

    if i ==1 or i==2:
        continue
    else:
        empty_lst.append(str(i))
n = "".join(empty_lst)
print(n,end="")

