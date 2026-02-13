if __name__=="__main__":
    user_input=int(input("Enter a number : "))
    user_input+=1
    for row in range(1,user_input):
        for sp in range(1,user_input-row):
            print(" ",end="")
        for col in range(1,row+1):
            #print(row,col)
            print("*",end="")
        print()