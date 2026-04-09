class Dog:
    def __init__(self,weight,name="XYZ",color="",breed=""):
        print("Inside Constructor")
        self.name = name
        self.weight = weight
        self.color = color
        self.breed = breed
    def eat(self,food):
        print(self.name," is eating")
        self.weight+=food
    def growl(self):
        print(self.name," Inside Growl")

if __name__=="__main__":
    d1=Dog(2,"Alice")
    d2=Dog(5,color="ABC")
    d1.eat(4)
    d2.eat(10)
    d1.growl()
    d2.growl()
    d1.eat(5)
    print("D2 Color ",d2.color)

