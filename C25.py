if __name__=="__main__":
    user_input=int(input("Enter a Number : "))
    for row in range(1,user_input+1):
        for sp in range(user_input-row):
            print(" ",end="")
        for col in range(1,row+1):
            print("*",end="")
        print()
