# mathlib/geometry.py

from math import pi

def area_circle(radius):
    return pi * (radius**2)


def perimeter_circle(radius):
    return 2 * pi * radius


def area_rectangle(length, width):
    return length * width


def perimeter_rectangle(length, width):
    return 2 * (length + width)