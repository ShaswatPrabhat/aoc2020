def treecount(paths, slope):
    if slope[1] > 1:
        paths = paths[::slope[1]]
        print(paths)
    width = len(paths[0])
    x = 0
    y = 0
    height = len(paths)
    count = 0
    for i in range(height - 1):
        x += slope[0]
        x = x % width
        y += 1
        if paths[y][x] == "#":
            count += 1
    return count


def get_number_of_trees(array):
    return treecount(array, [3, 1])


def create_array_from_input(readLines):
    matrix = []
    for w in readLines:
        a = []
        for character in w.strip():
            a.append(character)
        matrix.append(a)
    return matrix


if __name__ == '__main__':
    f = open('input_test.txt', 'r')

    print(get_number_of_trees(create_array_from_input(f.readlines())))
    f.close()
