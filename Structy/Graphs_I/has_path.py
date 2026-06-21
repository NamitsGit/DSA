# has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). 
# The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

from collections import deque


def has_path(graph, src, dst):
    # RECURSIVE
    # TIME : O(e) no of edges almost equal to n^2
    # SPACE : O(n) no of nodes
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst) == True:
            return True
    
    return False

    # ITERATIVE
    # TIME : O(e) no of edges almost equal to n^2
    # SPACE : O(n) no of nodes
    
    # queue = deque([ src ])
    # while queue:
    #     current = queue.popleft()

    #     if current == dst:
    #         return True
        
    #     for neighbour in graph[current]:
    #         queue.append(neighbour)
    # return False


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'j')) # False


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'i', 'h')) # True

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'w')) # True


graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'z')) # False
