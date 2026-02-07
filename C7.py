if __name__=="__main__":
    print("Hello World")
    cel_temp=input("Enter Cel Temp : ")
    cel_temp=float(cel_temp)
    far_temp=9/5 * cel_temp + 32
    print(far_temp)
    far_temp=int(far_temp)
    if far_temp>=90:
        print("Temp in 90's")
    elif far_temp>=80:
        print("Temp in 80's")
    elif far_temp>=70:
        print("Temp in 70's")
    else:
        print("Else- block")