class GraphWeighted:
    def __init__(self, graph):
        self._graph = {}
        for vertex in graph["nodes"]:
            self._graph[vertex] = set()
        for start, end, weight in graph["edges"]:
            self._graph[start].add((weight, end))
        
    def __iter__(self):
        for vertex in self._graph:
            for edge in self._graph[vertex]:
                yield (edge, vertex)
    
    def __str__(self):
        vertices = f"Vertices: {sorted(list(self._graph.keys()))}"       
        edges = "Edges:\n" + "\n".join(f'{start} -> {end} : {weight}' for (weight, end), start in self)
        return vertices + '\n' + edges
        
        
if __name__ == "__main__":
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

    graph = GraphWeighted(mesh)
    print(graph)

