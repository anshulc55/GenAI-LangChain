# Custom Module with Classes
import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)
    
    def circumference(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
