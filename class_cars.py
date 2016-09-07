#test commit1
import random
import operator

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
        self.km_reserve = self.max_run - self.trip_distance
        self.tank_refill()
        self.tachograph_check()
        self.ride()

    def every_nth_car(self):
        if Cars.car_count % 5 == 0 :
            self.tank = 75
    @property
    def define_trip_distance(self):      # setting trip distance
        self.trip_distance = random.randint(29000, 186000)
        return self.trip_distance

    def __str__(self):                  # set what we see when print instance
        return ('Distance passed {}, car cost {}, money for fuel {}, km in reserve {}, engine type is {}'.format(
        self.tachograph, self.car_cost, int(self.money_for_fuel), self.max_run - self.tachograph,self.engine_type))

    def __repr__(self):                # setting representation of instance
        return ('km in reserve {}, cost {}'.format(str(self.km_reserve),self.car_cost))

    def __add__(self, other):          # set car cost can add, also can write additional methods like radd
        return self.car_cost + other   # iadd

    def tank_refill(self):
        refilling_counter = 0
        refill = self.tank
        if int(self.tank) == 0:
            refilling_counter += 1
            self.tank = refill
        yield self.money_for_fuel, self.tank
        # print ('Refiling tank {} times'.format(refilling_counter))

    def tachograph_check(self):
        consume = self.consumption * 0.01
        decrease_count = 0
        if int(self.tachograph) % 1000 == 0:
            decrease_count += 1
            self.car_cost -= self.cost_lost
            self.consumption += consume
            if self.tachograph == self.max_run:
                print ('Car broke, stop moving')
            if self.car_cost <= 40:
                # raise ArithmeticError ('Car broke')
                self.trip_distance = 0
                self.km_reserve = 0
                print ("Car can't move its broke")
            yield self.tachograph, self.consumption, self.car_cost

    def ride(self):  # set what happens when car moving
        while self.trip_distance != 0:
            self.trip_distance -= 1
            self.tachograph += 1
            self.tank -= self.consumption / 10
            self.money_for_fuel += (self.consumption * self.fuel_price) / 10
        yield self.tachograph, self.trip_distance, self.tank, self.money_for_fuel

zaz = Cars()
zaz.ride()
print zaz.__dict__
print zaz
# car_pool = []
# gas_pool = []
# diesel_pool = []
# for x in range(0,5):
#     x = Cars()
#     x.ride()
#     car_pool.append(x)
# for car in car_pool:
#     if car.engine_type == 'Gas':
#         gas_pool.append(car)
#     else:
#         diesel_pool.append(car)

# print filter(lambda  x: x.km_reserve < 0, gas_pool)
# print sorted(gas_pool, key=operator.attrgetter('km_reserve'))
# print sorted(diesel_pool, key=operator.attrgetter('car_cost'))







