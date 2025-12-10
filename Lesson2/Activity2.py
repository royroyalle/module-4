def pal(r):
    e = len(r)-1
    s = 0
    while (s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = (1,2,3,3,2,1)
e = (1,2,1,2,1)
if (pal(r)):
    print("Tuple is a flip flop")
else:
    print("Not A flip flop")
if (pal(e)):
    print("Flip Flop")
else:
    print("Not A Flip Flop")