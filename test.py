class Car():
    def __init__(self):
        self.tank =20
        self.kms = 0

    def ride(self):
        while self.kms !=199:
            self.kms +=1
            self.tank -= 1
            yield self.tank

    def refill(self):
        if self.tank == 0:
            print ('Refilling')
            self.tank = 100
            return self.tank

car = Car()
car.ride()

print car.__dict__