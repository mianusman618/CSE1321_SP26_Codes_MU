class Dog:
    weight=0.0
    name=""
    breed=""
    gender=""
    color=""
    def eat(self,food):
        print(self.name," is eating")
        self.weight+=food

if __name__=="__main__":
    d1=Dog()
    d1.weight=4
    d1.name="Alice"
    d1.gender="M"

    d2=Dog()
    d2.weight=10
    d2.name="Bob"

    d1.eat(6)
    d2.eat(15)
    print("D1 Weight = ", d1.weight)
    print("D2 Weight = ", d2.weight)
    print(type(d1))

