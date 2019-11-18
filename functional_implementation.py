def explore_map(treasure_map, position=11):
    """
    Find path to treasure.
    :param position: starting position
    :return: path to treasure
    """
    # Check whether treasure map 5x5
    if len(treasure_map) != 5 or len(treasure_map[0]) != 5:
        return 0

    i, j = position // 10, position % 10
    value = treasure_map[i - 1][j - 1]
    path_to_treasure = [position]
    while True:
        if value == (i * 10 + j):
            return path_to_treasure
        else:
            i = value // 10
            j = value % 10
            path_to_treasure.append(value)
            value = treasure_map[i - 1][j - 1]


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

    result = explore_map(treasure_map)
    print(result)
