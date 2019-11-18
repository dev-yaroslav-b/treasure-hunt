import unittest

from oop_implementation import TreasureHunt


class TestTreasureHunt(unittest.TestCase):
    def setUp(self):
        self.treasure_hunt = TreasureHunt()

    def test_empty(self):
        treasure_map = [[]]
        self.treasure_hunt.set_map(treasure_map)
        self.assertEqual(self.treasure_hunt.explore_map(), 0)

    def test_different_size(self):
        treasure_map = [
            [55, 14, 25, 52],
            [44, 31, 11, 53],
            [24, 13, 45, 12],
            [42, 22, 43, 32]
        ]
        self.treasure_hunt.set_map(treasure_map)
        self.assertEqual(self.treasure_hunt.explore_map(), 0)

    def test_example(self):
        treasure_map = [
            [55, 14, 25, 52, 21],
            [44, 31, 11, 53, 43],
            [24, 13, 45, 12, 34],
            [42, 22, 43, 32, 41],
            [51, 23, 33, 54, 15]
        ]
        self.treasure_hunt.set_map(treasure_map)
        self.assertEqual(self.treasure_hunt.explore_map(), [11, 55, 15, 21, 44, 32, 13, 25, 43])


if __name__ == '__main__':
    unittest.main()
