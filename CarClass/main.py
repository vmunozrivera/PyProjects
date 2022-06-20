# Car Class
# Inheritance example with a car object
# TODO: Check inheritance in the base model

class Vehicle:
    color: str
    wheel: int
    door: int

    def __int__(self, color, wheel, door):
        self.color = color
        self.wheel = wheel
        self.door = door

    def __str__(self):
        return f'Color: {self.color}, Wheel: {self.wheel}, Doors: {self.door}'


class Car(Vehicle):
    speed: int
    cylinder: int

    def __int__(self, color="black", wheel=4, door=4, speed=None, cylinder=None):
        self.color = color
        self.wheel = wheel
        self.door = door
        self.speed = speed
        self.cylinder = cylinder

    def __str__(self):
        return f'Color: {self.color}, ' \
               f'Wheel: {self.wheel}, ' \
               f'Doors: {self.door}, ' \
               f'Speed: {self.speed}, ' \
               f'Cylinder: {self.cylinder}'


car = Car()
print(car)
