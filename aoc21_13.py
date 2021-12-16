""" fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6 """

raw_input = []
max_x = -1
max_y = -1

with open('aoc21_13_input.txt') as f:
    for line in f:
        raw_input.append(line)
        x,y = line.split(',')
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)

grid = []

for y in range(max_y):
    row = ['.'] * max_x
    grid.append(row)

for item in raw_input:
    x,y = item.split(',')
    grid[int(y)-1][int(x)-1] = '#'

def fold(grid, axis, line):
    current_height = len(grid)
    current_width = len(grid[0])

    if axis == 'x':
        new_grid = []
        for i in range(current_height):
            row = grid[i][0:line-1]
            new_grid.append(row)

        for y in range(current_height):
            for x in range(line, current_width):
                print(f'{x},{y}')
                if grid[y][x] == '#':
                    new_grid[y][current_width - x] = '#'
                    
    elif axis == 'y':
        new_grid = grid[0:line-1]
        for y in range(line, current_height):
            for x in range(current_width):
                if grid[y][x] == '#':
                    new_grid[current_height - y][x] = '#'

fold(grid, 'x', 655)

count = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            count += 1

print(count)