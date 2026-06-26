# undirected path
# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
# edges list will look like:
# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

def undirected_path(edges, node_A, node_B):
    graph = _create_graph(edges)
    print(graph)
    visited = set()
    result = _has_path(graph, visited, node_A, node_B)
    return result

def _create_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    return graph

def _has_path(graph, visited, src, dst):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)
    for neighbour in graph[src]:
        if _has_path(graph, visited, neighbour, dst):
            return True
    
    return False


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm')) # -> True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'm', 'j')) # -> True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'l', 'j')) # -> True


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'k', 'o')) # -> False

edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
]

print(undirected_path(edges, 'r', 't')) # -> True
