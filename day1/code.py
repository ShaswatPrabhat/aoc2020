from itertools import combinations


def get_pair_that_adds_to_2020(array_of_input):
    print(array_of_input)
    pair_wise_array = list(combinations(array_of_input, 2))

    for pair in pair_wise_array:
        if int(pair[0]) + int(pair[1]) == 2020:
            return int(pair[0]) * int(pair[1])

def get_triple_that_adds_to_2020(array_of_input):
    print(array_of_input)
    pair_wise_array = list(combinations(array_of_input, 3))

    for pair in pair_wise_array:
        if int(pair[0]) + int(pair[1]) + int(pair[2]) == 2020:
            return int(pair[0]) * int(pair[1]) * int(pair[2])


if __name__ == '__main__':
    f = open('input_real.txt', 'r')
    print(get_pair_that_adds_to_2020(f.readlines()))
