class Dog:
    def __init__(self,w,name="XYZ"):
        print("inside init")
        self.weight = w
        self.name = name
        self.rabid = True
        self.breed = ""
    def eat(self,food):
        print(self.name," is eating")
        self.weight+=food
    def growl(self):
        print(self.name ," in growl")

if __name__=="__main__":
    d1 = Dog(2.0,"Alice")
    d2 = Dog(1.0)
    print(type(d1))

    d1.eat(5)
    d2.eat(10)
    print("D1 weight = ", d1.weight)
    print("D2 weight = ", d2.weight)
    d1.growl()
    d2.growl()

