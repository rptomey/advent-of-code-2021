import sys

class Node:
    def __init__(self, x, y, risk):
        self.x = x
        self.y = y
        self.risk = risk
        self.neighbors = []

    def __str__(self):
        return f"{self.x},{self.y}"

# build the graph from the input file
counter_y = 0
counter_x = 0

graph = []

with open('aoc21_15_input.txt') as f:
    for line in f:
        row = []
        for bit in line:
            if bit != '\n':
                row.append(Node(counter_x, counter_y, int(bit)))
                counter_x += 1
        graph.append(row)
        counter_x = 0
        counter_y += 1

# go through the graph to identify each node's neighbors
graph_height = len(graph)
graph_width = len(graph[0])

for y_pos in range(graph_height):
    for x_pos in range(graph_width):
        current_node = graph[y_pos][x_pos]
        # add horizontal neighbors
        if current_node.x != 0:
            current_node.neighbors.append(graph[y_pos][x_pos-1])
        if current_node.x != graph_width - 1:
            current_node.neighbors.append(graph[y_pos][x_pos+1])
        # add vertical neighbors
        if current_node.y != 0:
            current_node.neighbors.append(graph[y_pos-1][x_pos])
        if current_node.y != graph_height - 1:
            current_node.neighbors.append(graph[y_pos+1][x_pos])

# setup for the algorithm
unvisited_nodes = []
for y_pos in range(graph_height):
    for x_pos in range(graph_width):
        unvisited_nodes.append(graph[y_pos][x_pos])

least_risk = {}
previous_nodes = {}

# set the starting node's total_risk to 0 and rest to maximum possible
starting_node = graph[0][0]
for node in unvisited_nodes:
    least_risk[str(node)] = sys.maxsize

least_risk[str(starting_node)] = 0

# loop until we've visited every node
while unvisited_nodes:
    current_min_node = None
    for node in unvisited_nodes:
        if current_min_node == None:
            current_min_node = node
        elif least_risk[str(node)] < least_risk[str(current_min_node)]:
            current_min_node = node

    # start looking at neighbors
    for neighbor in current_min_node.neighbors:
        temp_value = least_risk[str(current_min_node)] + current_min_node.risk
        if temp_value < least_risk[str(neighbor)]:
            least_risk[str(neighbor)] = temp_value
            previous_nodes[str(neighbor)] = current_min_node

    unvisited_nodes.remove(current_min_node)

print(least_risk[f'{graph_width-1},{graph_height-1}'] - graph[0][0].risk + graph[graph_height-1][graph_width-1].risk)
