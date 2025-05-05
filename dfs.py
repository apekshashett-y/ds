def dfs(graph, node, visited):
    print(node, end=' ')
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {}
nodes = input("Enter all nodes: ").split()

for node in nodes:
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

print(graph)

start = input("Enter starting node: ")
visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)
