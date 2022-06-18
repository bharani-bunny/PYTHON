"""
Write a program to implement single inheritance.
a. Create the parent class Circle. Initialise the constructor with the radius of the circle.
b. Define the method get_radius() and calc_area() to know the radius and area of the circle.
c. Create the child class named Cylinder. Initialise the value of the height within the constructor and call the constructor of the parent class to initialise the radius of the cylinder.
d. Finally, define the method Calc_area() in the class Cylinder to calculate the area of the cylinder.
Note: Area of Cylinder = 2 * pi * radius * height
"""

import math
class Circle:
    def __init__(self, r):
        self.r = r

    def get_radius():
        print("Radius = ", r)

    def calc_area():
        a = math.pi * r * r
        print("Area = ", a)


class Cylinder():
    def __init__(self, r, h):
        Circle.__init__(self, r)
        self.h = h

    def Calc_area(self):
        a = 2 * math.pi * r * h
        print("Area of the Cylinder : ",a)


r=int(input("Enter the radius of a cylinder : "))
h=int(input("Enter the height of a cylinder : "))
c=Cylinder(r,h)
c.Calc_area()

"""
output :
Enter the radius of a cylinder : 5
Enter the height of a cylinder : 6
Area of the Cylinder :  188.49555921538757
"""
