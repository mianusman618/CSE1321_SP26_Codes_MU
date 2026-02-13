if __name__=="__main__":
    user_input=int(input("Enter num of rows : "))
    for i in range(user_input):
        for j in range(user_input-i):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()