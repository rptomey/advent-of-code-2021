class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.flashed = False

grid = []
x_counter = 0
y_counter = 0
total_flashes = 0

# with open('aoc21_11_sample.txt') as f:
with open('aoc21_11_input.txt') as f:
    for line in f:
        row = []
        for n in line:
            if n != '\n':
                row.append(Octopus(x_counter, y_counter, int(n)))
                x_counter += 1
            else:
                x_counter = 0
                y_counter += 1
        grid.append(row)

# grid references are backwards: grid[y][x]

# need function for flashing
def flash(octo):
    global total_flashes
    total_flashes += 1
    global cycle_flashes
    cycle_flashes += 1
    x = octo.x
    y = octo.y
    octo.flashed = True

    # visit all of its neighbors and increase their energy
    for j in range(max(y-1, 0), min(10, y+2)):
        for i in range(max(x-1, 0), min(10, x+2)):
            grid[j][i].energy += 1
            if grid[j][i].energy > 9 and grid[j][i].flashed is False:
                flash(grid[j][i])

def cycle():
    # first, increase energy of all octopi by 1
    for y in range(10):
        for x in range(10):
            grid[y][x].energy += 1

    # make the octopi flash if energy greater than 9
    for y in range(10):
        for x in range(10):
            if grid[y][x].energy > 9 and grid[y][x].flashed is False:
                flash(grid[y][x])

    # reset energy of flashed octopi
    for y in range(10):
        for x in range(10):
            if grid[y][x].flashed:
                grid[y][x].energy = 0
                grid[y][x].flashed = False

# for i in range(100):
#     cycle()
# print(total_flashes)

# part 2 - how many cycles until they all flash at once?
cycle_counter = 0
cycle_flashes = 0

while cycle_flashes != 100:
    cycle_flashes = 0
    cycle_counter += 1
    cycle()

print(cycle_counter)