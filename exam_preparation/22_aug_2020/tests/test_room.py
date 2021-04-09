from unittest import TestCase, main

from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("RoomName", 100, 5)

    def test_if_attr_are_set(self):
        self.assertEqual("RoomName", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(5, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_init_when_expenses_is_negative_expect_raise(self):
        with self.assertRaises(ValueError) as context:
            self.room.expenses = -5
        self.assertEqual("Expenses cannot be negative", str(context.exception))

    def test_if_init_when_expenses_are_valid(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room.expenses)

    def test_calculate_expenses_when_zero_consumers_expect_zero_expenses(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_when_one_consumers_expect_to_be_correct(self):
        consumers = [TV()]
        self.room.calculate_expenses(consumers)
        self.assertEqual(consumers[0].get_monthly_expense(), self.room.expenses)

    def test_calculate_expenses_when_more_than_one_consumers_expect_to_be_correct(self):
        appliances = [TV()]
        children = [Child(5, 1, 2, 3)]

        self.room.calculate_expenses(appliances, children)
        expected = appliances[0].get_monthly_expense() + children[0].get_monthly_expense()
        self.assertEqual(expected, self.room.expenses)


if __name__ == '__main__':
    main()
