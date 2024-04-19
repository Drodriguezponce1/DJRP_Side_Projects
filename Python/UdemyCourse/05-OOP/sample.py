class Sample():

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self,name):
        self.name = name

    def toString(self):
        return f"My name is {self.name} and I am {self.age} years old!"

sam = Sample("Daniel", 26)

sam.setName("Danny")

print(sam.toString())

print(sam.getAge())