def is_safe(vertex, color):
    for neighbor in graph[vertex]:
        if neighbor in assignment and assignment[neighbor]==color:
            return False
    return True

def solve(vertex_list, index):
    if index == len(vertex_list):
        return True
    vertex = vertex_list[index]
    for color in colors:
        if is_safe(vertex, color):
            assignment[vertex] = color
            if solve(vertex_list, index+1):
                return True
            del assignment[vertex]
    return False

graph = {
    'A': ['B','D','C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B','A', 'C']
}
colors = ["Red","Green","Blue"]
vertex_list = list(graph.keys())
assignment = {}
if solve(vertex_list, 0):
    print("Solution Exists!")
    print("Color assignments : ")
    for vertex in vertex_list:
        print(f"{vertex} -> {assignment[vertex]}")
else:
    print("No solution found.")