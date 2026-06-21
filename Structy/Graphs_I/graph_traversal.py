
# Depth First Traversal in Graphs

from collections import deque


graph = {
    "a" : ["b", "c"],
    "b" : ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : []
}


def depth_first_print(garph, start):
    # ITERATIVE DFS
    # TIME : O(n)
    # SPACE : O(n)

    # stack = [ start ]

    # while stack:
    #     current = stack[-1]
    #     print(current)
    #     stack.pop()

    #     for neighbour in graph[current]:
    #         stack.append(neighbour)
    
    # RECURSIVE DFS
    # TIME : O(n)
    # SPACE : O(n)  
    print(start)

    for neighbour in graph[start]:
        depth_first_print(graph, neighbour)

def breadth_first_print(graph, start):
    # ITERATIVE (ALWAYS)
    # TIME : O(n)
    # SPACE : O(n)  
    queue = deque([start])

    while queue:
        current = queue.popleft()
        print(current)

        for neighbour in graph[current]:
            queue.append(neighbour)
    

print("DEPTH FIRST VALUES")
depth_first_print(graph, "a")

print("BREADTH FIRST VALUES")
breadth_first_print(graph, "a")
