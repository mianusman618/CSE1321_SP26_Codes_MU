if __name__=="__main__":
    print("Hello World")
    cel_temp=input("Enter Cel Temp : ")
    cel_temp=float(cel_temp)
    far_temp=9/5 * cel_temp + 32
    print(far_temp)
    far_temp=far_temp//10
    match far_temp:
        #90,91,92,93,94
        case 9:
            print("Temp in 90's")
        case 8:
            print("Temp in 80's")
        case 7:
            print("Temp in 70's")
        case _:
            print("Default case")