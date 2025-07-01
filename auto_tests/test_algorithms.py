import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scr/')))
from algorithms import Algorithm


# ---------- TSP Tests ----------

def test_tsp_positive_1():
    graph = {'A': {'B': 1, 'C': 2}, 'B': {'A': 1, 'C': 4}, 'C': {'A': 2, 'B': 4}}
    route, length = Algorithm.tsp(graph)
    assert route[0] == 'A' and route[-1] == 'A'
    assert len(route) == 4
    assert length > 0

def test_tsp_positive_2():
    graph = {
        'A': {'B': 1, 'C': 3, 'D': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 3, 'B': 2, 'D': 1},
        'D': {'A': 4, 'B': 5, 'C': 1}
    }
    route, length = Algorithm.tsp(graph)
    assert route[0] == 'A' and route[-1] == 'A'
    assert length > 0

def test_tsp_negative_1():
    graph = {'A': {'B': 1}, 'B': {}, 'C': {'A': 2}}
    route, length = Algorithm.tsp(graph)
    assert route == []
    assert length == float('inf')

def test_tsp_negative_2():
    graph = {'A': {}}
    route, length = Algorithm.tsp(graph)
    assert route == []
    assert length == float('inf')

# ---------- Dijkstra Tests ----------

def test_dijkstra_positive_1():
    graph = {'A': {'B': 1}, 'B': {'C': 2}, 'C': {'D': 3}, 'D': {}}
    path, length = Algorithm.dijkstra(graph, 'A', 'D')
    assert path == ['A', 'B', 'C', 'D']
    assert length == 6

def test_dijkstra_positive_2():
    graph = {'A': {'B': 1, 'C': 10}, 'B': {'C': 1}, 'C': {}}
    path, length = Algorithm.dijkstra(graph, 'A', 'C')
    assert path == ['A', 'B', 'C']
    assert length == 2

def test_dijkstra_negative_1():
    graph = {'A': {'B': 2}, 'B': {'C': 2}, 'C': {}, 'Z': {}}
    path, length = Algorithm.dijkstra(graph, 'A', 'Z')
    assert path is None
    assert length == "Путь не найден"

def test_dijkstra_negative_2():
    graph = {'A': {'B': 1}, 'B': {'C': 2}}
    path, length = Algorithm.dijkstra(graph, 'X', 'C')
    assert path is None
    assert length == "Путь не найден"

def test_dijkstra_negative_3():
    graph = {'A': {'B': 1}, 'B': {'C': 1}, 'C': {}}
    path, length = Algorithm.dijkstra(graph, 'A', 'C', max_length="abc")
    assert path == ['A', 'B', 'C']
    assert length == 2

# ---------- Kruskal Tests ----------

def test_kruskal_positive_1():
    graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'A': 1, 'C': 2, 'D': 4},
        'C': {'A': 5, 'B': 2, 'D': 1},
        'D': {'B': 4, 'C': 1}
    }
    mst = Algorithm.kruskal(graph)
    assert len(mst) == 3
    total_weight = sum(weight for _, _, weight in mst)
    assert total_weight == 4  # 1 + 1 + 2

def test_kruskal_positive_2():
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'C': 2},
        'C': {'A': 3, 'B': 2}
    }
    mst = Algorithm.kruskal(graph)
    assert len(mst) == 2  # для 3 вершин в MST будет 2 ребра
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 3  # минимальный вес остовного дерева

def test_kruskal_negative_1():
    graph = {'A': {'B': 1}, 'B': {'A': 1}, 'C': {}}
    mst = Algorithm.kruskal(graph)
    assert len(mst) == 1  # Только одно соединение

def test_kruskal_negative_2():
    graph = {}
    mst = Algorithm.kruskal(graph)
    assert mst == []

def test_kruskal_negative_3():
    graph = {'A': {'B': 1}, 'B': {'A': 1, 'C': 1}, 'C': {'B': 1, 'A': 1}}
    mst = Algorithm.kruskal(graph)
    assert len(mst) == 2  # Минимальное количество рёбер для связности 3 узлов
    weights = [w for _, _, w in mst]
    assert sum(weights) == 2

