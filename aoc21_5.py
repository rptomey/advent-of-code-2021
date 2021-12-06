from pprint import pprint as print
grid = [[0 for i in range(1000)] for j in range(1000)]

with open('aoc21_5_input.txt') as f:    
    for line in f:
        starting_coordinates = line.split(' -> ')[0]
        ending_coordinates = line.split(' -> ')[1]
        x1 = int(starting_coordinates.split(',')[0])
        y1 = int(starting_coordinates.split(',')[1])
        x2 = int(ending_coordinates.split(',')[0])
        y2 = int(ending_coordinates.split(',')[1])

        if x1 == x2:
            if y1 < y2:
                for y in range(y1,y2+1):
                    grid[x1][y] += 1
            elif y1 > y2:
                for y in range(y2,y1+1):
                    grid[x1][y] += 1
        elif y1 == y2:
            if x1 < x2:
                for x in range(x1,x2+1):
                    grid[x][y1] += 1
            elif x1 > x2:
                for x in range(x2,x1+1):
                    grid[x][y1] += 1
        else:
            while x1 != x2 and y1 != y2:
                grid[x1][y1] += 1
                if x2 > x1:
                    x1 += 1
                else:
                    x1 -= 1
                if y2 > y1:
                    y1 += 1
                else:
                    y1 -= 1
            
            grid[x2][y2] += 1

intersections = 0

for x in range(1000):
    for y in range(1000):
        if grid[x][y] > 1:
            intersections += 1

print(intersections)