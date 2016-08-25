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
        self.define_trip_distance()
        # self.tank_refill()
        #self.tachograph_check()
        #self.ride()

    def every_nth_car(self):
        if Cars.car_count % 5 == 0 :
            self.tank = 75

    def define_trip_distance(self):
        self.trip_distance = random.randint(29000, 186000)
        print (self.trip_distance)

    # def tank_refill(self):
    #     refilling_counter = 0
    #     refill = self.tank
    #     if self.tank <= 0:
    #         refilling_counter += 1
    #         self.tank = refill
    #     print ('Refiling tank {} times'.format(refilling_counter))

    # def tachograph_check(self):
    #     decrease_count = 0
    #     if int(self.tachograph) % 1000 == 0:
    #         decrease_count += 1
    #         self.car_cost -= self.cost_lost
    #         self.consumption *= 1.1
    #         if self.tachograph == self.max_run:
    #             print ('Car broke, stop moving')
    #     print ('Comsumption increase, car cost decrease {} times'.format(decrease_count))

    def ride(self):
        refilling_counter = 0
        refill = self.tank
        decrease_count = 0
        consume = self.consumption * 0.01
        while self.trip_distance!= 0:
            self.trip_distance -= 1
            self.tachograph += 1
            #self.tachograph_check()
            refill -= self.consumption / 10
            if int(refill) == 0:
                refilling_counter += 1
                refill = self.tank
            self.money_for_fuel += (self.consumption * self.fuel_price) / 100
            if int(self.tachograph) % 1000 == 0:
                decrease_count += 1
                self.car_cost -= self.cost_lost
                self.consumption += consume
                if self.tachograph == self.max_run:
                    print ('Car broke, stop moving')
        print ('Comsumption increase, car cost decrease {} times'.format(decrease_count))
        print ('Refiling tank {} times'.format(refilling_counter))
        



car = Cars()
car2 = Cars()
car3 = Cars()
car4 = Cars()
car.ride()
print (car.__dict__)
