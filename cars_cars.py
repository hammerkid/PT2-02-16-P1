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

    def __init__(self):
        Cars.car_count += 1
        super(self.__class__, self).__init__()
        self.tank = 60
        self.money_for_fuel = 0
        self.car_cost = 10000
        self.tachograph = 0
        self.every_nth_car()
        self.define_trip_distance
        #self.tank_refill()
        # self.tachograph_check()
        #self.ride()

    def every_nth_car(self):
        if Cars.car_count % 5 == 0 :
            self.tank = 75
    @property
    def define_trip_distance(self):
        self.trip_distance = random.randint(29000, 186000)
        return self.trip_distance

    def __str__(self):
        return ('Distance passed {}, car cost {}, money for fuel {}, km in reserve {}'.format(
        self.tachograph, self.car_cost, int(self.money_for_fuel), self.max_run - self.tachograph))


    # def tank_refill(self):
    #     refilling_counter = 0
    #     refill = self.tank
    #     if int(refill) == 0:
    #         refilling_counter += 1
    #         refill = self.tank
    #     self.money_for_fuel += (self.consumption * self.fuel_price) / 10
    #     print ('Refiling tank {} times'.format(refilling_counter))

    # def tachograph_check(self):
    #     consume = self.consumption * 0.01
    #     decrease_count = 0
    #     if int(self.tachograph) % 1000 == 0:
    #         decrease_count += 1
    #         self.car_cost -= self.cost_lost
    #         self.consumption += consume
    #         if self.tachograph == self.max_run:
    #             print ('Car broke, stop moving')
    #     print ('Comsumption increase, car cost decrease {} times'.format(decrease_count))

    def ride(self):
        refilling_counter = 0
        decrease_count = 0
        consume = self.consumption * 0.01
        refill = self.tank
        print self.trip_distance
        while self.trip_distance != 0:
            self.trip_distance -= 1
            self.tachograph += 1
            #self.tachograph_check()
            self.tank -= self.consumption / 10
            if int(self.tachograph) % 1000 == 0:
                decrease_count += 1
                self.car_cost -= self.cost_lost
                self.consumption += consume
                if self.tachograph == self.max_run:
                    print ('Car broke, stop moving')
            if int(self.tank) == 0:
                refilling_counter += 1
                self.tank = refill
            self.money_for_fuel += (self.consumption * self.fuel_price) / 10
        print ('Refiling tank {} times'.format(refilling_counter))
        print ('Comsumption increase, car cost decrease {} times'.format(decrease_count))









car = Cars()
car2 = Cars()
car3 = Cars()
car4 = Cars()
car5 = Cars()
car5.ride()
print (car5.__dict__)
print car5