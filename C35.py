def Usman(num1,num2=2,num3=3):
    print("Inside Sum Function")
    sum1=0
    for i in range(num2):
        sum1+=num1
    print(sum1)
if __name__=="__main__":
    print("Hello World")
    n1=2
    n2=5
    Usman(n1,n2)
    print("Back to main")