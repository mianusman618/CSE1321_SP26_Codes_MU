class Dog:
    name=""
    weight=0.0
    color=""
    breed=""
    def eat(self,food):
        print(self.name," is eating")
        self.weight+=food
    def growl(self):
        print(self.name," Inside Growl")

if __name__=="__main__":
    d1=Dog()
    d2=Dog()
    d1.name="Alice"
    d2.name="Bob"
    d1.weight=2
    d1.eat(4)
    d2.eat(10)
    d1.growl()
    d2.growl()
    d1.eat(5)

