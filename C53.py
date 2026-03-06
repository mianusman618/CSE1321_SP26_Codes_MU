def random_num(seed=2):
    randomnum=(seed+2)*2
    randomnum=int(randomnum%100)
    if randomnum<50:
        randomnum+=50
    return randomnum