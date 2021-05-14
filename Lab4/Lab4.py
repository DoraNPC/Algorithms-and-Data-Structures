from min_heap import PriorityQueue
from linked_list import SortedLinkedList

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

    def add_edge(self, edge):
        (length, end), start = edge
        if start not in self._graph:
            self._graph[start] = set()
        if end not in self._graph:
            self._graph[end] = set()
        self._graph[start].add((length, end))
        
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
                result.add_edge(edge)
                connect[start] |= connect[end]
        return result

    def Dijkstra(self, start):
        pathes = {v: [float("inf"), None] for v in self._graph}
        pathes[start] = [0, str(start)]
        priority_queue = PriorityQueue()
        for vertex in self._graph:
            priority_queue.insert(vertex, pathes[vertex])
        for _ in range(len(self._graph)):
            minimal = priority_queue.extract_min()
            vertex_weight, path = pathes[minimal]
            for edge_weight, vertex in self._graph[minimal]:
                if (weight := vertex_weight + edge_weight) < pathes[vertex][0]:
                    pathes[vertex][0] = weight
                    pathes[vertex][1] = path + str(vertex)
                    priority_queue.decrease_key(vertex, pathes[vertex])
        return pathes

    def Prim(self):
        queue = SortedLinkedList()
        length = len(self._graph)
        change = {k: v for k, v in zip(sorted(list(self._graph.keys())), range(length))}
        result = [[0 if i == j else None
            for i in range(length)]
            for j in range(length)]
        visited = set()
        start = set(self._graph.keys()).pop()
        visited.add(start)
        for edge in self._graph[start]:
            queue.add((edge, start))
        while queue:
            (weight, end), start = queue.get_min()
            if end not in visited:
                visited.add(end)
                result[change[start]][change[end]] = weight
                result[change[end]][change[start]] = weight
                for edge in self._graph[end]:
                    queue.add((edge, end))
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

    graph = GraphWeighted()
    graph.add_edge(((4, "b"), "a"))
    print(graph)

    graph = GraphWeighted(mesh1)
    result = graph.Kruskal()
    print(result)

    graph = GraphWeighted(mesh2)
    result = graph.Dijkstra("A")
    print(result)

    graph = GraphWeighted(mesh1)
    result = graph.Prim()
    print(result)