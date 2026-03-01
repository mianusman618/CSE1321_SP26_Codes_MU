def Usman(num1,num2=5):
    sum1=0
    for i in range(num2):
        sum1+=num1
    return sum1
    print(sum1)

if __name__=="__main__":
    print("Hello World")
    fun_output1=0
    fun_output2=0
    fun_output1=Usman(2,7)
    fun_output2=Usman(2)
    print("Back to main")
    print("Output 1",fun_output1)
    print("Output 2", fun_output2)
