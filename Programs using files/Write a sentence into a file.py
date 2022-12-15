
# Write a sentence into a file
lines = ['Read me ','How to write files']
with open('a.txt','w+') as f:
   for line in lines:
       f.write(line)
       f.write('\n')


