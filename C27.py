if __name__=="__main__":
    while True:
        print("Please Select an Operation (1-5) : ")
        print("1)- Add")
        print("2)- Sub")
        print("3)- Mul")
        print("4)- Divide")
        print("5)- Quit")
        user_choice=int(input("Enter Your Choice(1-5) : "))
        if user_choice==5:
            break
        elif user_choice==1:
            #print("Enter a number or 0 to stop :")
            result=0
            number=int(input("Enter a number or 0 to stop : "))
            while number!=0:
                result+=number
                print("Result = ",result)
                number = int(input("Enter a number or 0 to stop : "))
            print("Final Result is = ",result)
        elif user_choice==2:
            #print("Enter a number or 0 to stop :")
            result=0
            number=int(input("Enter a number or 0 to stop : "))
            while number!=0:
                result-=number
                print("Result = ",result)
                number = int(input("Enter a number or 0 to stop : "))
            print("Final Result is = ",result)
        elif user_choice==3:
            #print("Enter a number or 0 to stop :")
            result=1
            number=int(input("Enter a number or 0 to stop : "))
            while number!=0:
                result*=number
                print("Result = ",result)
                number = int(input("Enter a number or 0 to stop : "))
            print("Final Result is = ",result)
        elif user_choice==4:
            #print("Enter a number or 0 to stop :")
            number1=int(input("Enter a numenator : "))
            number2 = int(input("Enter a denomenator : "))


            print("Final Result is = ",number1/number2)
