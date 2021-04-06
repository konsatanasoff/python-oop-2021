import unittest

from lab.CarManager.car_manager import Car


class TestCar(unittest.TestCase):
    make = 'make'
    model = 'model'
    fuel_consumption = 10
    fuel_capacity = 100

    def __get_exception_from_init(self, make, model, fuel_consumption, fuel_capacity):
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        return context.exception

    def test_carInit_whenValidValues_shouldInitializeIt(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        expected = [self.make, self.model, self.fuel_consumption, self.fuel_capacity, 0]
        actual = [car.make, car.model, car.fuel_consumption, car.fuel_capacity, car.fuel_amount]

        self.assertListEqual(expected, actual)

    def test_carInit_whenNoneMake_shouldRaise(self):
        params = [None, self.model, self.fuel_consumption, self.fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenEmptyStringMake_shouldRaise(self):
        params = ["", self.model, self.fuel_consumption, self.fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNoneModel_shouldRaise(self):
        params = [self.make, None, self.fuel_consumption, self.fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenEmptyStringModel_shouldRaise(self):
        params = [self.make, "", self.fuel_consumption, self.fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelConsumption_shouldRaise(self):
        params = [self.make, self.model, -10, self.fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenZeroFuelConsumption_shouldRaise(self):
        params = [self.make, self.model, 0, self.fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelCapacity_shouldRaise(self):
        params = [self.make, self.model, self.fuel_consumption, -10]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenZeroFuelCapacity_shouldRaise(self):
        params = [self.make, self.model, self.fuel_consumption, 0]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelAmount_shouldRaise(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1

        self.assertIsNotNone(context.exception)

    def testCarRefuel_whenNegativeFuel_shouldRaise(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.refuel(-1)

        self.assertIsNotNone(context.exception)

    def testCarRefuel_whenZeroFuel_shouldRaise(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.refuel(0)

        self.assertIsNotNone(context.exception)

    def testCarRefuel_whenPositiveFuelAndEnoughInCapacity_shouldIcreaseAmount(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        car.refuel(5)
        self.assertEqual(5, car.fuel_amount)

    def testCarRefuel_whenPositiveFuelAndMoreThenCapacity_shouldSetAmountToCapacity(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        car.refuel(car.fuel_capacity * 2)
        self.assertEqual(self.fuel_capacity, car.fuel_amount)

    def test_carDrive_whenEnoughFuel_shouldDecreaseFuel(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        car.refuel(car.fuel_capacity)

        distance = 100
        car.drive(distance)
        expected = car.fuel_capacity - (distance / 100 * car.fuel_consumption)
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carDrive_whenNotEnoughFuel_shouldRaise(self):
        params = [self.make, self.model, self.fuel_consumption, self.fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.drive(100)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
