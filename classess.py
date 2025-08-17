class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("Move Along.!")

    def get_make_model(self):
        print(f"{self.make} {self.model} is moving.!")    


vehicle = Vehicle("Toyota", "Corolla")
vehicle.move()
vehicle.get_make_model()

class Airplane(Vehicle):
    def __init__(self, make, model, wingspan):
        super().__init__(make, model)
        self.wingspan = wingspan

    def get_make_model(self):
        print(f"{self.make} {self.model} is flying at a wingspan of {self.wingspan} meters.")

class Boat(Vehicle):
    def __init__(self, make, model, length):
        super().__init__(make, model)
        self.length = length

    def get_make_model(self):
        print(f"{self.make} {self.model} is sailing on water with a length of {self.length} meters.")

class Motorcycle(Vehicle):
    pass

airplane = Airplane("Boeing", "747", 68.4)
airplane.move()
airplane.get_make_model()
boat = Boat("Yamaha", "242X", 7.3)
boat.move()
boat.get_make_model()
motorcycle = Motorcycle("Harley-Davidson", "Street 750")
motorcycle.move()
motorcycle.get_make_model()

print("#######################################")

for v in (vehicle, airplane, boat, motorcycle):
    v.get_make_model()
    v.move()
