# Areas
# Calculate the areas of different geometry figures

import math

def triangle(b: float, h: float):
    """Calculate the area of a triangle"""
    a = (b*h)/2
    return a

def circle(r: float):
    """Calculate the area of a circle """
    a = math.pi*r**2
    return a


print(f'Triangle Area: { triangle(4, 5) }')
print(f'Circle Area: { round(circle(2),2) }')

