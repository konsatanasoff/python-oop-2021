import unittest

from lab.TestWorker.test_worker import Worker


class TestWorker(unittest.TestCase):
    name = "Test Worker"
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init__when_correct_args__expect_to_be_initialized(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_rest__expect_energy_increment(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker__when_energy_0_expect_exeption(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker__when_energy_above_0_expect_money_increase_by_salary(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.salary * 2, self.worker.money)

    def test_worker__when_energy_above_0_expect_energy_to_be_decremented(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info__expect_correct_value(self):
        expected_info = f'{self.name} has saved 0 money.'
        actual_info = self.worker.get_info()
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
