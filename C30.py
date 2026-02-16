if __name__=="__main__":
    user_input=int(input("Enter a Number : "))
    num=0
    for row in range(1,user_input+1):
        for col in range(1,row+1):
            print(num%user_input+1,end="")
            num+=1
        print()
    for row in range(user_input-1,0,-1):#range(4,0,-1)
        for col in range(row,0,-1):
            print(num%user_input+1,end="")
            num+=1
        print()