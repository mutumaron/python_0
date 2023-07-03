class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def speak(selfs):
        raise NotImplementedError("child classes must implimented")

class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meows"


#create object
dog=Dog("bosco","Brown")
print(dog.name)
print(dog.color)
print(dog.speak())

cat=Cat("Ron","Black")
print(cat.name)
print(cat.color)
print(cat.speak())

class Hyena(Animal):
    def speak(self):
         return "laughs"

hyena=Hyena("bosco2","Grey")
print(hyena.name)
print(hyena.color)
print(hyena.speak())