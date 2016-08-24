from itertools import count
import random
class Cars(object):
    car_count = 0

    def __init__(self, engine = 'Gas', tank = 60, car_cost = 10000, max_run = 200000, tachograph = 0,
                 money_for_fuel = 0, fuel_comsum = 8, fuel_price = 2.4 ):
        Cars.car_count += 1
        tank_75 = 75
        self.tank = tank
        self.money_for_fuel = money_for_fuel
        self.fuel_consum = fuel_comsum
        self.engine = engine
        self.car_cost = car_cost
        self.max_run = max_run
        self.fuel_price = fuel_price
        self.tachograph = tachograph
        if Cars.car_count % 3 == 0:
            self.engine = 'Diesel'
        if Cars.car_count % 5 == 0:
            self.tank = tank_75
        if self.engine == 'Diesel':
            self.fuel_price = 1.8
            self.max_run = 150000
            self.fuel_consum = 6

    def ride(self):
        fuel_left = self.tank
        self.path = random.randint(29000, 186000)
        print (self.path)
        if self.path > self.max_run:
            print ('Car to utilization')

        for km_100 in range(0, self.path, 100):
            print km_100
            self.tachograph += km_100
            self.tank -= self.fuel_consum
            self.money_for_fuel += self.fuel_price
            #print (self.tachograph)
            if self.tank <= 4:
                self.tank = fuel_left
                #print ('Tank is empty, refill')



car = Cars()
car2 = Cars ()
car3 = Cars ()
car4 = Cars()
car5 = Cars()
car6 = Cars()
car7 = Cars()
car8 = Cars()
car9 = Cars()
car10 = Cars()
print Cars.ride(car4)
print (car.ride(), car2.engine, car3.engine, car4.engine, car5.engine, car6.engine, car7.engine, car8.engine)
print (car.tank, car2.tank, car3.tank, car4.tank, car5.tank, car6.tank, car7.tank, car8.tank, car9.tank,car10.max_run)