input_array = []
counter = 0
alt_counter = 0
trio_counter = 0

with open('aoc21_1_input.txt') as f:
    for line in f:
        input_array.append(int(line.strip()))

for i in range(len(input_array)):
    if i >= 1:
        if input_array[i] > input_array[i-1]:
            counter += 1

for index, item in enumerate(input_array):
    if index >= 1:
        if item > input_array[index-1]:
            alt_counter += 1

for i in range(len(input_array)):
    if i >= 3:
        group_a = sum(input_array[i-2:i+1])
        group_b = sum(input_array[i-3:i])
        if group_a > group_b:
            trio_counter += 1

print(counter)
print(alt_counter)
print(trio_counter)