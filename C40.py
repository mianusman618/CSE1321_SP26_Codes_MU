def Usman(num1,num2=5):
    print("hello world")
    sum1=0
    for i in range(num2):
        sum1+=num1
    print(sum1)
if __name__=="__main__":
    print("in my main function")
    n1=2
    n2=5
    #fun_output=Usman(n1,n2)
    print(Usman(n1,n2))