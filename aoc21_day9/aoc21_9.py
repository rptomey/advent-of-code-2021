import math

class Point:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.neighbors = []
        self.neighbor_heights = []
        self.assigned = False

    def __str__(self):
        return f"Height {self.height} @ Coordinate {self.x}, {self.y}"

    def low_bool(self):
        return self.height < min(self.neighbor_heights)

points = []
x_counter = 0
y_counter = 0

with open('aoc21_9_input.txt') as f:
    for line in f:
        for n in line:
            if n != '\n':
                points.append(Point(x_counter, y_counter, int(n)))
                x_counter += 1
            else:
                x_counter = 0
                y_counter += 1

# find neighbors for each point
for point in points:
    neighboring_points = [candidate for candidate in points if abs(point.x - candidate.x) + abs(point.y - candidate.y) == 1]
    point.neighbors = neighboring_points
    point.neighbor_heights = [neighbor.height for neighbor in neighboring_points]

# find and sum low point risk level values
risk_sum = 0

for point in points:
    if point.low_bool():
        risk_sum += point.height + 1

print(risk_sum)

# assign points and their neighbors to basins
basins = []

def build_basin(point):
    basin = []
    queue = []
    
    evaluate_point(basin, queue, point)
    
    if len(basin) > 0:
        basins.append(basin)

def evaluate_point(basin, queue, point):
    if point.height < 9:
        basin.append(point)
        point.assigned = True
    
    for neighbor in point.neighbors:
        if neighbor not in queue:
            queue.append(neighbor)
            if neighbor.assigned is False and neighbor.height < 9:
                evaluate_point(basin, queue, neighbor)

for point in points:
    if point.assigned is False and point.height < 9:
        build_basin(point)

top_basins = [0] * 3

for basin in basins:
    b_len = len(basin)
    if b_len > max(top_basins):
        top_basins.insert(0, b_len)
        top_basins.pop()
    elif b_len > top_basins[1]:
        top_basins.insert(1, b_len)
        top_basins.pop()
    elif b_len > top_basins[2]:
        top_basins.insert(2, b_len)
        top_basins.pop()

print(math.prod(top_basins))