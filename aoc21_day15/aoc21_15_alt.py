import math
import sys

graph = {}
x_counter = 0
y_counter = 0

with open('aoc21_15_input.txt') as f:
    for line in f:
        for c in line:
            if c == '\n':
                x_counter = 0
                y_counter += 1
            else:
                graph[f'{x_counter},{y_counter}'] = int(c)
                x_counter += 1

# make it big
big_graph = graph.copy()
original_size = math.sqrt(len(graph))

# add or loop function for expanding graph
def add_or_loop(number, iteration):
    new_number = number + iteration
    if new_number > 9:
        return new_number - 9
    else:
        return new_number

# widen first
for i in range(1,5):
    for key, value in graph.items():
        x_str,y_str = key.split(',')
        new_x = int(int(x_str) + (original_size * i))
        new_y = int(y_str) # may not be necessary, but just to be consistent in a few rows...
        new_risk = add_or_loop(value, i)
        big_graph[f'{new_x},{new_y}'] = new_risk

# then taller
bigger_graph = big_graph.copy()
for i in range(1,5):
    for key, value in big_graph.items():
        x_str,y_str = key.split(',')
        new_x = int(float(x_str)) # again maybe unnecessary, but whatever...
        new_y = int(int(y_str) + (original_size * i))
        new_risk = add_or_loop(value, i)
        bigger_graph[f'{new_x},{new_y}'] = new_risk

def dijkstra(graph, start, target, size):
    nodes = list(graph)
    least_risk = {}
    previous_node = {}

    for node in nodes:
        least_risk[node] = sys.maxsize
        previous_node[node] = ''
    least_risk[start] = 0

    while nodes:
        current_node = None
        for node in nodes:
            if current_node == None:
                current_node = node
            elif least_risk[node] < least_risk[current_node]:
                current_node = node

        print(len(nodes))
        nodes.remove(current_node)

        # end early if we've reached the target
        if current_node == target:
            break

        # find the node's neighbors
        current_x,current_y = current_node.split(',')
        int_x = int(current_x)
        int_y = int(current_y)

        neighbors = []
        if int_x > 0:
            neighbors.append(f'{int_x - 1},{int_y}')
        if int_x < (size - 1):
            neighbors.append(f'{int_x + 1},{int_y}')
        if int_y > 0:
            neighbors.append(f'{int_x},{int_y - 1}')
        if int_y < (size - 1):
            neighbors.append(f'{int_x},{int_y + 1}')
        
        # get distances for neighbors still in queue
        for neighbor in neighbors:
            if neighbor in nodes:
                risk = least_risk[current_node] + graph[neighbor]
                if risk < least_risk[neighbor]:
                    least_risk[neighbor] = risk
                    previous_node[neighbor] = current_node

    return least_risk, previous_node

# calculate small graph
""" origin = '0,0'
destination = f'{int(original_size - 1)},{int(original_size - 1)}'
size = original_size
risks, priors = dijkstra(graph, origin, destination, size)
print(risks[destination]) """

# calculate big graph
origin = '0,0'
destination = f'{int(original_size * 5 - 1)},{int(original_size * 5 - 1)}'
size = original_size * 5
risks, priors = dijkstra(bigger_graph, origin, destination, size)
print(risks[destination])