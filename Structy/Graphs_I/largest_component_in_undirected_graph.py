# largest component
# Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
# The function should return the size of the largest connected component in the graph.

def largest_component(graph):
    visited = set()
    largest_ = 0
    for node in graph:
        curr_comp_size = component_size(graph, node, visited)
        largest_ = max(largest_, curr_comp_size)
    return largest_


def component_size(graph, current, visited):
    if current in visited:
        return 0
    
    visited.add(current)
    count = 1

    for neighbour in graph[current]:
        count += component_size(graph, neighbour, visited)
    
    return count

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # 4

print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # 6

print(largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # 5

print(largest_component({})) # -> 0

print(largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
})) # -> 3

print(largest_component({
  3: []
})) # -> 1

