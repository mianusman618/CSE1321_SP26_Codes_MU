def Usman(num1,num2=5):
    print("hello world")
    sum=0
    for i in range(num2):
        sum+=num1
    print(sum)
if __name__=="__main__":
    print("in my main function")
    n1=2
    n2=3
    Usman(n1,n2)
    Usman()