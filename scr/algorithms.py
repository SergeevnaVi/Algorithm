import itertools
import heapq
import time

class Algorithm:
    @staticmethod
    def tsp(graph: dict) -> tuple:
        vertices = list(graph.keys())
        min_length = float("inf")
        best_route = []
        found_route = False

        for perm in itertools.permutations(vertices):
            length = 0
            valid_route = True
            for i in range(len(perm) - 1):
                if perm[i+1] in graph[perm[i]]:
                    length += graph[perm[i]][perm[i+1]]
                    time.sleep(0.0001)
                else:
                    valid_route = False
                    break
            # Возврат в начальную точку
            if valid_route and perm[0] in graph[perm[-1]]:
                length += graph[perm[-1]][perm[0]]
                time.sleep(0.0001)
            else:
                valid_route = False

            if valid_route and length < min_length:
                min_length = length
                best_route = list(perm) + [perm[0]]
                found_route = True

        if found_route:
            return best_route, min_length
        else:
            return [], float('inf') # Возвращаем пустой путь и бесконечность, если маршрут не найден

    @staticmethod
    def dijkstra(graph: dict, start: str, end: str, max_length: str = None) -> tuple:
        """Алгоритм Дейкстры для поиска кратчайшего пути"""
        vertices = set(graph.keys())
        for neighbors in graph.values():
            vertices.update(neighbors.keys())
        distances = {vertex: float('inf') for vertex in vertices} # Инициализация всех вершин
        previous = {vertex: None for vertex in vertices}
        distances[start] = 0
        queue = [(0, start)]

        max_len = float('inf') if max_length is None or not max_length.isdigit() else float(max_length)

        while queue:
            current_dist, current_vertex = heapq.heappop(queue)

            if current_vertex == end:
                path = []
                while current_vertex:
                    path.insert(0, current_vertex)
                    current_vertex = previous[current_vertex]
                return path, distances[end]

            if current_dist > max_len:
                continue  # Если текущая длина пути уже превышает ограничение, пропускаем

            if current_vertex in graph: # Проверка, существует ли вершина в графе
                for neighbor, weight in graph[current_vertex].items():
                    distance = current_dist + weight
                    time.sleep(0.0001)
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_vertex
                        heapq.heappush(queue, (distance, neighbor))

        return None, "Путь не найден"
    
    @staticmethod
    def kruskal(graph: dict) -> list:
        """Алгоритм Крускала для построения минимального остовного дерева"""
        parent = {}
        rank = {}

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]

        def union(v1, v2):
            root1, root2 = find(v1), find(v2)
            if root1 != root2:
                if rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    if rank[root1] == rank[root2]:
                        rank[root1] += 1

        # Инициализация
        for vertex in graph:
            parent[vertex] = vertex
            rank[vertex] = 0

        edges = []
        for v1 in graph:
            for v2 in graph[v1]:
                if (v2, v1, graph[v1][v2]) not in edges:
                    edges.append((v1, v2, graph[v1][v2]))

        # Сортировка рёбер
        edges.sort(key=lambda x: x[2])
        mst = []

        for v1, v2, weight in edges:
            time.sleep(0.0001)
            if find(v1) != find(v2):
                union(v1, v2)
                mst.append((v1, v2, weight))

        return mst