class Circle():

    pi = 3.14 # use these for final instance variables like java
    li = []
    def __init__(self, radius=1): # 1 is default
        self.radius = radius
        self.li.append(radius)

    def get_circumference(self):
        return self.radius * self.pi * 2
    

circle = Circle(2)
cir = Circle()

print(circle.li)

print(f"Circumference of this object is {circle.get_circumference()}")