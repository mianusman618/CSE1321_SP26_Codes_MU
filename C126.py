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
    def print_info(self):
        print("Name ",self.name)
        print("Weight ",self.weight)

if __name__=="__main__":
    d1=Dog()
    d1.name="Alice"
    d1.weight=23
    d1.print_info()
    Dog.weight=50
    d2=Dog()
    d1.print_info()
    d2.print_info()


