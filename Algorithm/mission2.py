class Car():
    def __init__(self,fuel,wheels):
        self.fuel = fuel
        self.wheels = wheels

class Bike(Car):
    def __init__(self,fuel,wheels,size):
        super().__init__(fuel, wheels)
        self.size = size

bike = Bike("gas",2,"small")
print(bike.size)