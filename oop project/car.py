class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name=name
        self.fuelRate=0
        self.velocity=0
        self.fuelRate=fuelRate
        self.velocity=velocity


    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self,value):
        if value<0:
            self._fuelRate=0
        elif value>100:
            self._fuelRate=100
        else:
            self._fuelRate=value

    @property
    def velocity(self):
        return self._velocity


    @velocity.setter
    def velocity(self, value):
        if value < 0:
            self._velocity = 0
        elif value > 200:
            self._velocity = 200
        else:
            self._velocity = value

    
    def run(self,velocity,distance):
        self.velocity=velocity
        print(f'{self.name} is now running at {self.velocity} Km/h')

        fuel_needed=distance / 10
        if fuel_needed > self.fuelRate:
            max_distance=self.fuelRate*10
            remaining=distance - max_distance
            self.fuelRate=0
            print(f"{self.name} ran out of fuel after {max_distance} km.")
            self.stop(remaining)
        else:
            self.fuelRate -= fuel_needed
            print(f"{self.name} completed {distance} km. Remaining fuel: {self.fuelRate:.1f}%.")
            self.stop(0)

    def stop(self,remaining_distance=0):
        self.velocity=0
        if remaining_distance > 0:
            print(f"{self.name} stopped with {remaining_distance} km remaining.")
        else:
            print(f"{self.name} has arrived at the destination!")

    
    def __str__(self):
        return (f"Car: {self.name}\n"
                f"Fuel: {self.fuelRate}%\n"
                f"Velocity: {self.velocity} km/h")