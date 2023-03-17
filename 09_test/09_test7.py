# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.

class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def speed(self):
        print(self.max_speed)


class bus(vehicle):
	def print(self):
		print("vehicle speed:",self.max_speed)
		print("vehicle mileage:",self.mileage)



b1 = vehicle(200, 50000)



v1 = vehicle(120,30)


bus1 = bus(250, 50)
bus1.speed()

 
