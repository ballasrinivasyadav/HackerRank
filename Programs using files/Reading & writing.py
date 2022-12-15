# Reading & writing in files

file1 = open('a.txt','r')

file2 = open('b.txt','w')
l = ['This is Delhi \n','this is paris \n','This is london \n']

file2.write('hello\n')
file2.writelines(l)
file2.close()


