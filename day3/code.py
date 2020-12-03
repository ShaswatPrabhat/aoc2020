def is_valid(line):
    split_col = line.split(':')
    password = split_col[1].strip()
    test_clause = split_col[0]
    number_clause = test_clause.split(' ')[0]
    character_clause = test_clause.split(' ')[1]
    min = int(number_clause.split('-')[0]) - 1
    max = int(number_clause.split('-')[1]) - 1
    if password[min] == character_clause and password[max] != character_clause:
        return True
    elif password[max] == character_clause and password[min] != character_clause:
        return True
    else:
        return False

def get_valid_sets(array_of_input):
    counter = 0
    for line in array_of_input:
        if is_valid(line):
            counter += 1
    return counter


if __name__ == '__main__':
    f = open('input_real.txt', 'r')
    print(get_valid_sets(f.readlines()))
