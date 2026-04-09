class Dog:
    def __init__(self,w,name="XYZ"):
        print("Inside init")
        self.weight=w
        self.name=name
    def eat(self,food):
        print(self.name," is eating")
        self.weight+=food

if __name__=="__main__":
    d1=Dog(2)
    d2=Dog(3)
    d2.name="Bob"

    d1.eat(6)
    d2.eat(15)
    print("D1 Weight = ", d1.weight)
    print("D2 Weight = ", d2.weight)
    print(type(d1))
    d1.eat(1)

