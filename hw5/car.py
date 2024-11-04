class Car:
    def __init__(self, yearModel: int, make: str):
        self.yearModel = yearModel
        self.make = make
        self.speed = 0
    def accelerate(self):
        self.speed = self.speed + 5

    def brake(self):
        self.speed = self.speed - 5
car = Car(2005, 'Supra')
print("Let's accelerate: \n")
for i in range(0, 5):
    car.accelerate()
    print("Speed: ", car.speed)
    pass
for i in range(0, 5):
    car.brake()
    print("Speed: ", car.speed)
