if __name__=="__main__":
    while True:
        print("Please Select (1-5) ")
        print("1)- Add")
        print("2)- Sub")
        print("3)- Mul")
        print("4)- Divide")
        print("5)- Quit")
        user_choice=int(input("Enter Your Choice  : "))
        if user_choice==5:
            break
        elif user_choice==1:
            print("You have selected add (+) op")
            result=0
            while True:
                number =int(input("Enter a number or zero(0) to stop : "))
                if number==0:
                    break
                result+=number
            print("Final Result is = ",result)
        elif user_choice==2:
            print("You have selected subtract (-) op")
            result=0
            while True:
                number =int(input("Enter a number or zero(0) to stop : "))
                if number==0:
                    break
                result-=number
            print("Final Result is = ",result)
        elif user_choice==3:
            print("You have selected Multiply (*) op")
            result=1
            while True:
                number =int(input("Enter a number or zero(0) to stop : "))
                if number==0:
                    break
                result*=number
            print("Final Result is = ",result)
        elif user_choice==4:
            print("You have selected Divide (/) op")
            number1 = int(input("Enter a number1  : "))
            number2 = int(input("Enter a number2  : "))
            print("Final Result is = ",number1/number2)