graph = {}

with open('aoc21_12_input.txt') as f:
# with open('aoc21_12_sample.txt') as f:
    for line in f:
        a,b = line.strip().split('-')
        if a not in graph:
            graph[a] = [b]
        else: graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else: graph[b].append(a)

def lowercase_repeated(path):
    for node in path:
        if node.islower():
            if path.count(node) > 1:
                return True
    return False

# https://www.python.org/doc/essays/graphs/
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper() or (not lowercase_repeated(path) and node != 'end' and node != 'start'):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

all_paths = find_all_paths(graph, 'start', 'end')

print(len(all_paths))