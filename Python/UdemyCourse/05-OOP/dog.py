class Dog():

    #class object attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self.spots = 0

    def bark(self):
        print(f"Woof! my name is {self.name}, and I am a {self.breed}")

myDog = Dog("Golden Retriever", "Max")

myDog.bark()

print(myDog.spots)

