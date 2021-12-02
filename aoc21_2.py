horizontal_position = 0
vertical_position = 0
aim = 0
        
def move(direction, distance):
    global horizontal_position 
    global vertical_position
    if direction == "forward":
        horizontal_position += distance
    elif direction == "down":
        vertical_position += distance
    elif direction == "up":
        vertical_position -= distance
    else:
        print(f"unrecognized input: {direction} {distance}")

def aimed_move(direction, distance):
    global horizontal_position 
    global vertical_position
    global aim

    if direction == "down":
        aim += distance
    elif direction == "up":
        aim -= distance
    elif direction == "forward":
        horizontal_position += distance
        vertical_position += (distance * aim)
    else:
        print(f"unrecognized input: {direction} {distance}")

def cased_move(direction, distance):
    global horizontal_position 
    global vertical_position
    global aim

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

with open('aoc21_2_input.txt') as f:
    for line in f:
        direction = line.split()[0]
        distance = int(line.split()[1])
        cased_move(direction, distance)

print(f"final position reached. horizontal: {horizontal_position}, vertical: {vertical_position}")
print(f"position product = {horizontal_position * vertical_position}")