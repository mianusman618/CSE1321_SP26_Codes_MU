if __name__=="__main__":
    user_input=int(input("Enter a positive number : "))
    for row in range(1,user_input+1):
        for col in range(1,row+1):
            print("*",end="")
        print()