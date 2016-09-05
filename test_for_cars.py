import unittest
from cars_cars import Cars

class TestNthCarTank(unittest.TestCase):

    def setUp(self):
        tank = 60



    def test_gas_tank(self):
        for car in range(2):
            car = Cars()
            self.assertEquals(60, car.tank)
            self.assertEqual('Gas', car.engine_type)

    def test_ride(self):
        car = Cars()
        car.ride()
        self.assertNotEqual(0, car.tachograph)
        self.assertNotEqual(0, car.money_for_fuel)



if __name__ == '__main__':
    unittest.main()



