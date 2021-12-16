folds = []
with open('aoc21_13_folds.txt') as f:
    for line in f:
        axis,number = line.strip().split('=')
        folds.append({'axis':axis, 'line':int(number)})

coordinates = []
with open('aoc21_13_input.txt') as f:
    for line in f:
        x,y = line.strip().split(',')
        coordinates.append({'x':int(x),'y':int(y)})

for fold in folds:
    temp_coordinates = []

    for coordinate in coordinates:
        if coordinate[fold['axis']] < fold['line']:
            temp_coordinates.append(coordinate)
        if coordinate[fold['axis']] > fold['line']:
            new_coordinate = coordinate
            new_coordinate[fold['axis']] = fold['line'] * 2 - coordinate[fold['axis']]
            temp_coordinates.append(new_coordinate)

    coordinates = temp_coordinates
    # break - for part one answering dots after first fold

# figure out what's unique
coordinate_strings = []
for coordinate in coordinates:
    string = f'{coordinate["x"]},{coordinate["y"]}'
    if string not in coordinate_strings:
        coordinate_strings.append(string)

# print(len(coordinate_strings))