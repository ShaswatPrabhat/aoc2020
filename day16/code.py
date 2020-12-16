my_test_data = [2, 0, 6, 12, 1, 3]
last_index_found_set = {}

for i, n in enumerate(my_test_data):
    if i != len(my_test_data) - 1:
        last_index_found_set[n] = i

while len(my_test_data) < 30000000:
    previous = my_test_data[-1]
    prev_prev = last_index_found_set.get(previous, -1)
    last_index_found_set[previous] = len(my_test_data) - 1
    if prev_prev == -1:
        next_entry = 0
    else:
        next_entry = len(my_test_data) - 1 - prev_prev
    my_test_data.append(next_entry)
    if len(my_test_data) == 2020:
        print(next_entry)
print(my_test_data[-1])
