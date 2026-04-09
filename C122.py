class Dog:
    weight=0.0
    name=""
    rabid=True
    breed=""
    def eat(self,food):
        print(self.name," is eating")
        self.weight+=food
    def growl(self):
        print(self.name ," in growl")

if __name__=="__main__":
    d1=Dog()
    d2=Dog()
    print(type(d1))
    d1.weight=2.0
    d1.name="Alice"
    d2.name="Bob"

    d1.eat(5)
    d2.eat(10)
    print("D1 weight = ",d1.weight)
    print("D2 weight = ", d2.weight)
    d1.growl()
    d2.growl()
