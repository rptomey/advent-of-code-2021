class Point:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.neighbor_heights = []

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
    
    point.neighbor_heights = [neighbor.height for neighbor in neighboring_points]

# find and sum low point risk level values
risk_sum = 0

for point in points:
    if point.low_bool():
        risk_sum += point.height + 1

print(risk_sum)