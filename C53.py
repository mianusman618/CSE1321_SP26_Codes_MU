def random_num(seed):#4
    randomnum=(seed+2)*2
    randomnum=int(randomnum%100)#10%100=10
    if randomnum<50:
        randomnum+=50
    return randomnum
def myabs(i):
    if i<0:
        i*=-1
    return i