if __name__=="__main__":
    count=1
    while True:
        if count==4:
            print("inside if")
            break
        print("Iteration # ",count)
        count+=1
    print("rest of the program")