
# ODD-EVEN splitting

def split(mix):
    ev = []
    od = []
    an = []
    for i in mix:
        if i%2==0:
            ev.append(i)
        else:
            od.append(i)
    print(ev)
    print(od)
mix = [1,2,3,4,5,6,7,8,9,10]
split(mix)
