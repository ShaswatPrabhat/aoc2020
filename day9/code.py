puzzle = list(map(int, open('input_real.txt').read().splitlines()))

part_1 = part_2 = None
for idx in range(25, len(puzzle)):
    prev = puzzle[idx - 25: idx]
    if not any(num_1 + num_2 == puzzle[idx] and num_1 != num_2
               for num_1 in prev for num_2 in prev):
        part_1 = puzzle[idx]
        break
print(part_1)

for end_idx in range(len(puzzle)):
    for start_idx in range(end_idx):
        puzzle_slice = puzzle[start_idx: end_idx]
        slice_sum = sum(puzzle_slice)
        if slice_sum < part_1:
            break
        elif slice_sum == part_1:
            part_2 = min(puzzle_slice) + max(puzzle_slice)
    if part_2:
        break
print(part_2)
