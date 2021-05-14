from Lab4 import GraphWeighted

mesh = {
    "nodes": {"A", "B", "C", "D", "E", "F"},
    "edges": {
        ("A", "B", 5),
        ("A", "C", 2),
        ("B", "D", 6),
        ("C", "D", 4),
        ("C", "F", 3),
        ("D", "E", 1),
        ("F", "E", 7),
    }
}

#For Kruskal and Prim's algorithms we will use undirected graph
mesh_undirected = {
    "nodes": {"A", "B", "C", "D", "E"},
    "edges": {
        ("A", "B", 3),
        ("B", "A", 3),
        ("C", "B", 5),
        ("B", "C", 5),
        ("B", "E", 1),
        ("E", "B", 1),
        ("C", "D", 6),
        ("D", "C", 6),
        ("A", "D", 4),
        ("D", "A", 4),
        ("A", "E", 2),
        ("E", "A", 2),
        ("E", "D", 7),
        ("D", "E", 7),
    }
}

mesh2 = {
    "nodes": {"A", "B", "C", "D", "E", "F"},
    "edges": {
        ("A", "B", 1),
        ("A", "D", 8),
        ("A", "F", 3),
        ("B", "C", 6),
        ("B", "D", 3),
        ("C", "D", 5),
        ("D", "E", 4),
        ("D", "F", 7),
        ("E", "F", 2),
        ("F", "C", 3),
    }
}

graph = GraphWeighted(mesh)
print(graph)
print()

graph = GraphWeighted()
graph.add_edge(((4, "b"), "a"))
print("Add edge:")
print(graph)
print()

graph = GraphWeighted(mesh_undirected)
result = graph.Kruskal()
print("Kruskal algorithm:")
print(result)
print()

graph = GraphWeighted(mesh2)
result = graph.Dijkstra("A")
print("Dijkstra algorithm:")
for vertex, (weight, path) in result.items():
    print(f"For node {vertex} path {path} with weight {weight}")
print()

graph = GraphWeighted(mesh_undirected)
result = graph.Prim()
print("Prim's algorithm:")
for raw in result:
    print(raw)