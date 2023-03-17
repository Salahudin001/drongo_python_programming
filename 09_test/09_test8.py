# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.


class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Bus", 180, 12)
print(f"{School_bus.color} {School_bus.name}, Speed: {School_bus.max_speed}, Mileage: {School_bus.mileage}")

car = Car("Audi Q7", 240, 18)
print(f"{car.color} {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}")