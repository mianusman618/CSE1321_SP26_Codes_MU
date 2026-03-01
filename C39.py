def Usman(num1,num2=5):
    var1=2
    print("hello world")
    sum1=0
    for i in range(num2):
        sum1+=num1
    #print(sum1)
    return sum1
if __name__=="__main__":
    print("in my main function")
    n1=2
    n2=3
    #fun_result=Usman(n1,n2)#50
    print(Usman(n1,n2))