from functional_implementation import explore_map


def test_empty():
    treasure_map = [[]]
    assert explore_map(treasure_map) == 0


def test_different_size():
    treasure_map = [
        [55, 14, 25, 52],
        [44, 31, 11, 53],
        [24, 13, 45, 12],
        [42, 22, 43, 32]
    ]

    assert explore_map(treasure_map) == 0


def test_example():
    treasure_map = [
        [55, 14, 25, 52, 21],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15]
    ]
    assert explore_map(treasure_map) == [11, 55, 15, 21, 44, 32, 13, 25, 43]


