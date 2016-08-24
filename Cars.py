from itertools import count
import random
class Cars(object):
    car_count = 0

    def __init__(self, engine = 'Gas', tank = 60, car_cost = 10000, max_run = 200000, tachograph = 0,
                 money_for_fuel = 0, fuel_comsume = 8.0, fuel_price = 2.4):
        Cars.car_count += 1
        tank_75 = 75
        self.tank = tank
        self.money_for_fuel = money_for_fuel
        self.fuel_consume = fuel_comsume
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
            self.fuel_consume = 6.0

    @property
    def ride(self):
        if self.tachograph > self.max_run:
            print('Car to utile')
        return self.tachograph

    @ride.setter
    def ride(self, path):
        if path > self.max_run:
            return 'Car to utile'
        refill = self.tank
        self.tachograph += 1
        if self.engine == 'Gas':
            self.tank -= self.fuel_consume / 100
            self.money_for_fuel += 0.192
        else:
            self.tank -= self.fuel_consume / 100
            self.money_for_fuel += 0.108
        if self.tank <= 0:
            self.tank = refill
            print ('Refilling tank')
        if self.tachograph % 1000 == 0:
            self.fuel_consume += self.fuel_consume / 100
            if self.engine == 'Gas':
                self.car_cost -= 100
            else:
                self.car_cost -= 120






car = Cars()

print (car.ride(100))
# car.tachograph, '-Tacho', car.fuel_consum,'-Consume', car.car_cost,'-Car price', car.money_for_fuel,'-Money for fuel')
#print (car.tank, car2.tank, car3.tank, car4.tank, car5.tank, car6.tank, car7.tank, car8.tank, car9.tank,car10.max_run)
