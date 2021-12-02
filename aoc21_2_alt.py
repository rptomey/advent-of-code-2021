horizontal_position = 0
vertical_position = 0
aim = 0

with open('aoc21_2_input.txt') as f:
    for line in f:
        direction = line.split()[0]
        distance = int(line.split()[1])

        match direction:
            case "down":
                aim += distance
            case "up":
                aim -= distance
            case "forward":
                horizontal_position += distance
                vertical_position += (distance * aim)
            case _:
                print(f"unrecognized input: {direction} {distance}")

print(f"final position reached. horizontal: {horizontal_position}, vertical: {vertical_position}")
print(f"position product = {horizontal_position * vertical_position}")