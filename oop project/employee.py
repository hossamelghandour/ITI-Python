from person import Person
from car import Car


class Employee(Person):
    def __init__(self,id,name, money, mood, healthRate):
        super().__init__(name, money, mood, healthRate)
        self.id=id

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self,car:Car,velocity,distance):
        print(f"{self.name} is driving {car.name}.")
        car.run(velocity, distance)
    

    def refuel(self,car:Car,gasAmount=100):
        car.fuelRate = car.fuelRate+gasAmount
        if car.fuelRate > 100:
            car.fuelRate=100


