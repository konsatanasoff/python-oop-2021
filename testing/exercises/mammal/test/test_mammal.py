from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("mammal_name", "mammal_type", "mammal_sound")
        self.kingdom = self.mammal.__class__.get_kingdom(self.mammal)

    def test_if_attr_are_set(self):
        self.assertEqual("mammal_name", self.mammal.name)
        self.assertEqual("mammal_type", self.mammal.type)
        self.assertEqual("mammal_sound", self.mammal.sound)
        self.assertEqual("animals", self.kingdom)

    def test_mammal_kingdom_initial(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if__it_makes_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_if_get_kingdom(self):
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_info_str_correct(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()
