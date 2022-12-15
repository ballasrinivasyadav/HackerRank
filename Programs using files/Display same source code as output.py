
# Display same source code as output
#
# def f(str='print(lambda str=%r: (str %% str))()'):
#     return str % str
# print(f())
# def f1(str='print(lambda str=%r: (str %% str))()'):
#     return str % str
# print(f1())

def file_copy(a, b):
    with open(a) as f, open(b, 'w') as d:
        d.write(f.read())
        file_copy("untitled0.py", "z.py")
        with open('z.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end='')

