import random

class Engine(object):
    engine_count = 0
    def __init__(self):
        Engine.engine_count += 1
        self.engine_type = 'Gas'
        self.consumption = 8.0                  # liters per kilometer
        self.max_run = 200000
        self.fuel_price = 2.4
        self.cost_lost = 100
        if Engine.engine_count % 3 == 0:
            self.engine_type = 'Diesel'
            self.consumption = 6.0               # liters per kilometer
            self.max_run = 150000
            self.fuel_price = 1.8
            self.cost_lost = 120

class Cars(Engine):
    car_count = 0
    def __init__(self, car_cost = 10000, tachograph = 0, money_for_fuel = 0):
        Cars.car_count += 1
        super(self.__class__, self).__init__()
        self.tank = 60
        self.money_for_fuel = money_for_fuel
        self.car_cost = car_cost
        self.tachograph = tachograph
        #self.path = random.randint(29000, 186000)
        if Cars.car_count % 5 == 0:
            self.tank = 75
        self.define_trip_distance()

    # @staticmethod
    # def get_distance():
    #     Cars.distance_traveled = xrange(29000, 186000,1)
    #          return distance_traveled
    def define_trip_distance(self):
        self.trip_distance = random.randint(29000, 186000)

    def ride(self):
        while self.trip_distance != 0:
            self.trip_distance -=1
            refill = self.tank
            self.tachograph += 1
            self.tank -= self.consumption
            self.money_for_fuel += (self.consumption * self.fuel_price) / 100
            print self.tank
            if int(self.tank) <= 0:
                print ('Refill tank')
                self.tank = refill
            if int(self.tachograph) % 1000 == 0:
                self.car_cost -= self.cost_lost
                self.consumption = self.consumption * 1.1
                print ('Comsumption increase, car cost decrease.')
            if self.tachograph == self.max_run:
                print ('Car broke, stop moving')










car = Cars()
car2 = Cars()
car3 = Cars()
car4 = Cars()
car3.ride()
print (car3.__dict__)
