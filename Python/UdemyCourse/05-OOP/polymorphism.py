class Dog():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"

#=================================================================================

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"



dog = Dog("Danny")
cat = Cat("Felix")

print(dog.speak())
print(cat.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(dog)