class Animal():

    def __init__(self):
        print("ANIMAL CREATED!")

    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating!")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created!")

    def who_am_i(self):
        print("I am a dog")

dog = Dog()

dog.who_am_i()

