from lark import Lark, LarkError


def solve_with_parser(part='part1'):
    parser_rules, input_data = open('input_real.txt').read().split('\n\n')
    source_map = '0123456789'
    destination_map = 'abcdefghij'
    if part == 'part2':
        parser_rules = parser_rules.replace('8: 42', '8: 42 | 42 8')
        parser_rules = parser_rules.replace('11: 42 31', '11: 42 31 | 42 11 31')

    parser_rules = parser_rules.translate(str.maketrans(source_map, destination_map))
    print('parser_rules', parser_rules)

    parser = Lark(parser_rules, start='a')

    total = 0
    for line in input_data.splitlines():
        try:
            parser.parse(line)
            total += 1
        except LarkError:
            print("Fails for -->", line)
            pass
    return total


if __name__ == "__main__":
    print('result for part1-->', solve_with_parser('part1'))
    print('result for part2-->', solve_with_parser('part2'))
