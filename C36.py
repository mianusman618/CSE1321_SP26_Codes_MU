def fun2():
    print("Inside func 2")

def Usman(num1,num2=5):
    print("Inside function")
    fun2()
    print("Back to Usman Function")
    sum1=0
    for i in range(num2):
        sum1+=num1
    print(sum1)
if __name__=="__main__":
    print("Hello World")
    Usman(2,7)
    Usman(2)
    print("Back to main")
