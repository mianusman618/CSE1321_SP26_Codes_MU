if __name__=="__main__":
    user_input=int(input("Enter a number : "))
    for row in range(1,user_input+1):
        for col in range(row):
            print("*",end="")
        print()