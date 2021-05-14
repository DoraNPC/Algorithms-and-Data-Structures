class GraphWeighted:
    def __init__(self, graph=None):
        self._graph = {}
        if graph is not None:
            for vertex in graph["nodes"]:
                self._graph[vertex] = set()
            for start, end, weight in graph["edges"]:
                self._graph[start].add((weight, end))
        
    def __iter__(self):
        for vertex in self._graph:
            for edge in self._graph[vertex]:
                yield (edge, vertex)
    
    def __str__(self):
        vertices = "Vertices:\n" f"{sorted(list(self._graph.keys()))}"       
        edges = "Edges:\n" + "\n".join(f'{start} -> {end} : {weight}' for (weight, end), start in self)
        return vertices + '\n' + edges

    def add_edge_undirect(self, edge):
        (length, end), start = edge
        if start not in self._graph:
            self._graph[start] = set()
        if end not in self._graph:
            self._graph[end] = set()
        self._graph[start].add((length, end))
        self._graph[end].add((length, start))
        
    def Kruskal(self):
        edges = []
        for start, pathes in self._graph.items():
            for path in pathes:
                edges.append((path, start))
        edges.sort()
        
        connect = {v: {v} for v in self._graph}
        
        result = GraphWeighted()
        for edge in edges:
            (_, end), start = edge
            if connect[start] != connect[end]:
                result.add_edge_undirect(edge)
                connect[start] |= connect[end]
                connect[end] = connect[start]
        return result

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

    mesh1 = {
        "nodes": {"A", "B", "C", "D", "E"},
        "edges": {
            ("A", "B", 3),
            ("B", "C", 5),
            ("B", "E", 1),
            ("C", "D", 6),
            ("A", "D", 4),
            ("A", "E", 2),
            ("E", "D", 7),
        }
    }

    graph = GraphWeighted(mesh)
    print(graph)

    graph = GraphWeighted()
    graph.add_edge_undirect(((4, "b"), "a"))
    print(graph)

    graph = GraphWeighted(mesh1)
    result = graph.Kruskal()
    print(result)