if __name__=="__main__":
    count=1
    while count<10:
        if count==4:
            print("Inside if ")
            count += 1
            continue
        print("Iteration ",count)
        count+=1
    print("Outside loop rest of the program")