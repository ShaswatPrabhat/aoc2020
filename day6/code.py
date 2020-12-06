answers = open('input_test.txt').read().replace('\r\n', '\n').replace('\n\n', '|').replace('\n', ' ').split('|')

part1 = 0
part2 = 0

for answer in answers:
    part1 += len(set(answer.replace(' ', '')))
    part2 += len(set.intersection(*map(set, answer.split())))
    print(answer, '--->', list(map(set, answer.split())))

print(f'Part 1: {part1}, Part 2: {part2}')
