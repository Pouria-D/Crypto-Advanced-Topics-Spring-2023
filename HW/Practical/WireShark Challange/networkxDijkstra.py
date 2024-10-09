import networkx as nx

edges = [
    (1, 2, {"weight": 2}),
    (1, 3, {"weight": 3}),
    (1, 4, {"weight": 4}),
    (2, 1, {"weight": 2}),
    (2, 4, {"weight": 1}),
    (3, 1, {"weight": 3}),
    (4, 1, {"weight": 1}),
    (4, 2, {"weight": 1}),
]

G = nx.Graph()
for i in range(1, 5):
    G.add_node(i)
G.add_edges_from(edges)

pos = nx.planar_layout(G)

# This will give us the shortest path from node 1 to node 4.
p1to4 = nx.shortest_path(G, source=1, target=4, weight="weight")
print("Shortest path from 1 to 4: ", p1to4)

# This will give us the length of the shortest path from node 1 to node 4.
length = nx.shortest_path_length(G, source=1, target=4, weight="weight")
print("Length of the shortest path: ", length)