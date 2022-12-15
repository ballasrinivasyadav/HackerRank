
# Compare two text/data files

import difflib

with open('a.txt') as f1:
    f1_txt = f1.readlines()

with open('b.txt') as f2:
    f2_txt = f2.readlines()

for line in difflib.unified_diff(
    f1_txt,f2_txt,fromfile='a.txt',
    tofile='b.txt',lineterm=''):
    print(line)
