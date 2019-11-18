class TreasureHunt(object):
    def __init__(self):
        self.treasure_map = [[]]
        self.path_to_treasure = []

    def set_map(self, treasure_map):
        """
        Set treasure map.
        :param treasure_map: our treasure map which is the nested list
        :return:
        """
        self.treasure_map = treasure_map

    def explore_map(self, position=11):
        """
        Find path to treasure.
        :param position: starting position
        :return: path to treasure
        """
        # Check whether treasure map 5x5
        if len(self.treasure_map) != 5 or len(self.treasure_map[0]) != 5:
            return 0
        # Add starting position to path
        if not len(self.path_to_treasure):
            self.path_to_treasure.append(position)

        value = self.treasure_map[position // 10 - 1][position % 10 - 1]
        if value == position:
            return self.path_to_treasure
        else:
            self.path_to_treasure.append(value)
            return self.explore_map(value)


if __name__ == '__main__':
    treasure_map = [
        [55, 14, 25, 52, 21],
        [44, 31, 11, 53, 43],
        [24, 13, 45, 12, 34],
        [42, 22, 43, 32, 41],
        [51, 23, 33, 54, 15]
    ]

    for t in treasure_map:
        print(t)

    treasure_hunt = TreasureHunt()
    treasure_hunt.set_map(treasure_map)
    result = treasure_hunt.explore_map()
    print(result)
