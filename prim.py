def prim(graph, start):
    mst = [start] 
    mst_edges = []  

    while len(mst) < len(graph):
        min_edge = None
        for node in mst:
            for neighbor, weight in graph[node]:
                if neighbor not in mst: 
                    if min_edge is None or weight < min_edge[2]:  
                        min_edge = (node, neighbor, weight)
        mst_edges.append(min_edge)
        mst.append(min_edge[1])  
    return mst, mst_edges

graph = {
    'A': [('B', 2), ('C', 6)],
    'B': [('A', 2), ('D', 3)],
    'C': [('A', 6), ('D', 1), ('E', 5)],
    'D': [('B', 3), ('C', 1), ('E', 4)],
    'E': [('C', 5), ('D', 4)]
}

mst, mst_edges = prim(graph, 'A')

total_weight = sum(edge[2] for edge in mst_edges)

print("Nodes in the Minimal Spanning Tree (MST):", mst)
print("Edges in the Minimal Spanning Tree (MST):")
for edge in mst_edges:
    print(f"{edge[0]} - {edge[1]} (weight: {edge[2]})")
print(f"Total weight of the MST: {total_weight}")