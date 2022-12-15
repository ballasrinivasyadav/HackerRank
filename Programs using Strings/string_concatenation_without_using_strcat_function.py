
# string concatenation without using strcat function

n = 's'
m ='dd'
print("The string is:",n,"and:",m)
o = ("".join([n,m]))
print(o)
print('%s%s'%(n,m))
print("{}{}".format(n,m))

