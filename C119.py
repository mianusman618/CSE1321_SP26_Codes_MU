class Dog:
    def __init__(self,w,r=True,n="XYZ"):
        self.rabid = r
        self.w = w
        self.name = n
    def growl(self):
        print("Inside growl ",self.name)
    def eat(self,num):
        print((self.name," is eating"))
        self.weight+=num
    def print_info(self):
        print(self.name," ",self.w," ",self.rabid)

if __name__=="__main__":
    d1=Dog(5)
    d2=Dog(10,False,"Bob")
    d1.growl()
    d2.growl()
    d1.print_info()
    d2.print_info()