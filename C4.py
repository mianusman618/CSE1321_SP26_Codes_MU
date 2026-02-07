if __name__=="__main__":
    print("Hello World")
    #Country US and age is 18
    u_country=input("Is your county US (Y/N) : ")
    if u_country == 'Y' or u_country=='y':
        age=int(input("Enter age : "))
        if age>=21:
            u_id=input("Do you have your ID with you (Y/N) : ")
            if u_id=='Y':
                print("Allowed to drink ")
            else:
                print("You need to have id to buy")
        else:
            print("Not Allowed to drink")
    else:
        print("Drinking laws unknown")

print("Outside of main")