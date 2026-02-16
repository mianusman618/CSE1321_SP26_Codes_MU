if __name__=="__main__":
    number=0
    user_input=int(input("Enter a Number : "))
    for row in range(1,user_input+1):
        for col in range(1,row+1):
            print(number%user_input+1,end="")
            number+=1
        print()
    for row in range(user_input-1,0,-1):
        for col in range(row+1,1,-1):
            print(number % user_input + 1, end="")
            number += 1
        print()