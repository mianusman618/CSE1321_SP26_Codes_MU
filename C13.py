from itertools import count

if __name__=="__main__":
    count=1
    while count<10:
        if count==4:
            print("inside if")
            count += 1
            continue
        print("Iteration # ",count)
        count+=1
    print("rest of the program")