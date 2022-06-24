import pickle

class Car:

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def __str__(self):
        return self.color + " " + self.speed


my_car = Car("Black", "140")
print(my_car)

file = open('car-settings', 'w+b')

pickle.dump(my_car, file)

file.seek(0)
load_settings = pickle.load(file)

print(load_settings)
file.close()