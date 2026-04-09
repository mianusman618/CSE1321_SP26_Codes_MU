class Dog:
    rabid = False
    weight = 0
    name = ""
    def growl(self):
        print("Inside growl ",self.name)
    def eat(self,num):
        print((self.name," is eating"))
        self.weight+=num
    def print_info(self):
        print(self.name," ",self.weight," ",self.rabid)

if __name__=="__main__":
    d1=Dog()
    Dog.rabid=True
    Dog.weight=200
    d2=Dog()
    d1.print_info()
    d2.print_info()
    # d1.name="Alice"
    # d2=Dog()
    # d2.name="bob"
    # d1.growl()
    # d2.growl()