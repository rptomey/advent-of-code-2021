input_row_count = 0
input_array = []
gamma_array = []
epsilon_array = []

with open('aoc21_3_input.txt') as f:
    for line in f:
        input_array.append(str(line.strip()))
    
array_length = len(input_array[0])

for n in range(array_length):
    gamma_array.append(0)

for item in input_array:
    for n in range(array_length):
        gamma_array[n] += int(item[n])
    input_row_count += 1
    
print(f'Rows processed: {input_row_count}')
print(f'Raw gamma_array: {gamma_array}')

for n in range(array_length):
    if gamma_array[n] / input_row_count > 0.5:
        gamma_array[n] = 1
        epsilon_array.append(0)
    else:
        gamma_array[n] = 0
        epsilon_array.append(1)

print(f'Processed gamma_array: {gamma_array}')
print(f'Processed epsilon_array: {epsilon_array}')

gamma_string = "".join(str(num) for num in gamma_array)
epsilon_string = "".join(str(num) for num in epsilon_array)

gamma_decimal = int(gamma_string,2)
epsilon_decimal = int(epsilon_string,2)

print(f'Gamma decimal: {gamma_decimal}')
print(f'Epsilon decimal: {epsilon_decimal}')

print(f'Product of gamma * epsilon: {gamma_decimal * epsilon_decimal}')

o2_generator_input = input_array
co2_scrubber_input = input_array.copy()

for position in range(array_length):
    position_sum = 0

    for n in range(len(o2_generator_input)):
        position_sum += int(o2_generator_input[n][position])
    
    if position_sum / len(o2_generator_input) >= 0.5:
        position_target = "1"
    else:
        position_target = "0"

    for n in reversed(range(len(o2_generator_input))):
        if len(o2_generator_input) <= 1:
            break
        current_value = o2_generator_input[n]
        if current_value[position] != position_target:
            del o2_generator_input[n]

print(f"Final o2_generator_input: {o2_generator_input}")

for position in range(array_length):
    position_sum = 0

    for n in range(len(co2_scrubber_input)):
        position_sum += int(co2_scrubber_input[n][position])
    
    if position_sum / len(co2_scrubber_input) < 0.5:
        position_target = "1"
    else:
        position_target = "0"

    for n in reversed(range(len(co2_scrubber_input))):
        if len(co2_scrubber_input) <= 1:
            break
        current_value = co2_scrubber_input[n]
        if current_value[position] != position_target:
            del co2_scrubber_input[n]

print(f"Final co2_scrubber_input: {co2_scrubber_input}")

o2_generator_decimal = int(o2_generator_input[0],2)
co2_scrubber_decimal = int(co2_scrubber_input[0],2)

print(f'O2 Generator decimal: {o2_generator_decimal}')
print(f'CO2 Scrubber decimal: {co2_scrubber_decimal}')

print(f'Product of 02 Generator * CO2 Scrubber: {o2_generator_decimal * co2_scrubber_decimal}')