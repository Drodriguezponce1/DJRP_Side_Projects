import math

class Line():

    def __init__(self,coor1,coor2):

        points = list(coor1) + list(coor2)
        self.x1 = points[0]
        self.y1 = points[1]
        self.x2 = points[2]
        self.y2 = points[3]

        #remember you can unpack a tuple by doing
        # x1,y1 = coor1

    def distance(self):
        return math.sqrt( math.pow(self.x2-self.x1,2) + math.pow(self.y2 - self.y1,2)              )

    def slope(self):
        return (self.y2- self.y1) / (self.x2 - self.x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#Problem 2

class Cylinder():

    pi = 3.14

    def __init__(self,height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * (self.radius**2) * self.height

    def surface_area(self):
        return (2 * self.pi * self.radius * self.height) + (2 * self.pi * (self.radius ** 2))
    

cylinder = Cylinder(2,3)

print(cylinder.volume())
print(cylinder.surface_area())