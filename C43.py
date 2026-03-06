import time as t
def myMethod():
    print("inside function in file c43")

def randnum(max_num):
    print("inside function 2 random num")
    seconds=t.time()
    return int(seconds%max_num)+int(seconds%5)