if __name__=="__main__":
    while True:
        print("Please Select (1-4) ")
        print("1)- Add")
        print("2)- Sub")
        print("3)- Mul")
        print("4)- Divide")
        print("5)- Quit")
        user_choice=int(input("Enter your choice : "))
        if user_choice==5:
            print("Going to Exit")
            break
        elif user_choice==1:
            print("You selected Add(+) Op ")
            result=0
            while True:
                num=int(input("Enter a number or Zero(0) to stop : "))
                result+=num
                if num==0:
                    break
            print("Final Result is = ",result)
        elif user_choice==2:
            print("You selected Sub(-) Op ")
            result=0
            while True:
                num=int(input("Enter a number or Zero(0) to stop : "))
                result-=num
                if num==0:
                    break
            print("Final Result is = ",result)
        elif user_choice==3:
            print("You selected Mul(*) Op ")
            result=1
            while True:
                num=int(input("ppppEnter a number or Zero(0) to stop : "))
                if num==0:
                    break
                result*=num

            print("Final Result is = ",result)
        elif user_choice==4:
            print("You selected Mul(*) Op ")
            result=1
            while True:
                num=int(input("ppppEnter a number or Zero(0) to stop : "))
                if num==0:
                    break
                result*=num

            print("Final Result is = ",result)
