import random


class Car:
    color = "red"
    max_speed = 0  # in km/h
    velocity = 0  # in km/h
    heading = 0  # in degrees
    traveltime = 0  # in seconds

    def __init__(self):
        """When this class is instantiated, generate some interesting actual random values"""
        self.color = random.choice(["green", "yellow", "white", "blue"])
        self.heading = random.randint(0, 360)
        self.max_speed = random.randint(0, 400)
        self.velocity = random.randint(0, self.max_speed)
        self.traveltime = random.randint(0, 1000)

    def traveled_distance(self):
        """calculates the distance this car traveled given the time and velocity"""
        result = self.velocity * (self.traveltime / 3600)  # in km
        return result

    def print_properties(self):
        print(self.color + " " + str(self.velocity) + "km/h " + str(
            self.heading) + "deg " + str(self.traveled_distance()) + "km")


car1 = Car()
car2 = Car()

car1.print_properties()
car2.print_properties()


car1 = Car()
car1.color = "blue"
car1.velocity = 50
car1.heading = 10

car2 = Car()
car2.color = "green"
car2.velocity = 45.5
car2.heading = 18

car3 = Car()
car3.color = "yello"
car3.velocity = 52
car3.heading = 16

car4 = Car()
car4.color = "orange"
car4.velocity = 54
car4.heading = 15

car5 = Car()
car5.color = "red"
car5.velocity = 48
car5.heading = 11

print(car1.color)
