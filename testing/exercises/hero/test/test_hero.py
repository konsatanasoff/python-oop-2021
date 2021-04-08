from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.main_hero = Hero("Main Hero", 5, 100, 10)
        self.other_hero = Hero("Other Hero", 10, 90, 30)

    def test_check_attr_are_set(self):
        self.assertEqual("Main Hero", self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

        self.assertEqual("Other Hero", self.other_hero.username)
        self.assertEqual(10, self.other_hero.level)
        self.assertEqual(90, self.other_hero.health)
        self.assertEqual(30, self.other_hero.damage)

    def test_battle_raises_if_fight_self(self):
        hero_self = Hero("Main Hero", 6, 101, 11)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(hero_self)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_not_enough_raises(self):
        self.main_hero.health = 0
        self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.other_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_is_less_than_zero_raises(self):
        self.other_hero.health = -5
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.other_hero)
        self.assertEqual("You cannot fight Other Hero. He needs to rest", str(ex.exception))

    def test_fight_draw_case(self):
        self.other_hero.health = 50
        result = self.main_hero.battle(self.other_hero)

        self.assertEqual("Draw", result)

    def test_fight_lose_case(self):
        self.other_hero.health = 100
        result = self.main_hero.battle(self.other_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(35, self.other_hero.damage)
        self.assertEqual(11, self.other_hero.level)
        self.assertEqual(55, self.other_hero.health)
        self.assertTrue(self.main_hero.health < 0)

    def test_fight_win_case(self):
        self.main_hero.damage = 100
        self.main_hero.health = 500
        result = self.main_hero.battle(self.other_hero)

        self.assertEqual("You win", result)
        self.assertEqual(105, self.main_hero.damage)
        self.assertEqual(6, self.main_hero.level)
        self.assertEqual(205, self.main_hero.health)

    def test_str_represent(self):
        self.assertEqual("Hero Main Hero: 5 lvl\nHealth: 100\nDamage: 10\n", str(self.main_hero))


if __name__ == '__main__':
    main()
