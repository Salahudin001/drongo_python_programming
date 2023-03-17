
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def speed(self):
        print("speed")


v1 = vehicle(355, 35)
print("max speed is", v1.max_speed)
print("mileage is ", v1.mileage)
