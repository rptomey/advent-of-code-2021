with open('aoc21_7_input.txt') as f:
    contents = f.read()

crabs = [int(c) for c in contents.split(',')]
# crabs = [16,1,2,0,4,2,7,1,2,14]
best_position = -1
lowest_fuel = -1

""" for i in range(min(crabs), max(crabs)):
    fuel_sum = 0
    for crab in crabs:
        fuel_sum += abs(crab - i)
    if fuel_sum < lowest_fuel or lowest_fuel == -1:
        lowest_fuel = fuel_sum
        best_position = i """

for i in range(min(crabs), max(crabs)):
    print(i)
    fuel_sum = 0
    for crab in crabs:
        distance = abs(crab - i)
        if distance > 0:
            fuel_cost = 0
            for j in range(1, distance+1):
                fuel_cost += j
            fuel_sum += fuel_cost
            
    if fuel_sum < lowest_fuel or lowest_fuel == -1:
        lowest_fuel = fuel_sum
        best_position = i

print(f'Best position: {best_position}')
print(f'Fuel sum: {lowest_fuel}')