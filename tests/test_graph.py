"""Tests for graph algorithms."""

import pytest

from algorithms.graph import bfs, dfs, dijkstra, kruskal_mst, prim_mst, shortest_path

# ---------------------------------------------------------------------------
# Sample graphs
# ---------------------------------------------------------------------------
UNWEIGHTED = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2],
}

WEIGHTED = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [],
}

UNDIRECTED_WEIGHTED = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)],
}


# ---------------------------------------------------------------------------
# BFS
# ---------------------------------------------------------------------------
def test_bfs_visits_all_nodes():
    visited = bfs(UNWEIGHTED, 0)
    assert sorted(visited) == [0, 1, 2, 3, 4]


def test_bfs_order():
    visited = bfs(UNWEIGHTED, 0)
    # 0 must be first; its direct neighbours 1 and 2 must come before 3 and 4
    assert visited[0] == 0
    assert set(visited[1:3]) == {1, 2}


def test_bfs_single_node():
    assert bfs({0: []}, 0) == [0]


def test_bfs_disconnected():
    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    visited = bfs(graph, 0)
    assert sorted(visited) == [0, 1]


# ---------------------------------------------------------------------------
# DFS
# ---------------------------------------------------------------------------
def test_dfs_visits_all_nodes():
    visited = dfs(UNWEIGHTED, 0)
    assert sorted(visited) == [0, 1, 2, 3, 4]


def test_dfs_order():
    visited = dfs(UNWEIGHTED, 0)
    assert visited[0] == 0


def test_dfs_single_node():
    assert dfs({0: []}, 0) == [0]


def test_dfs_disconnected():
    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    visited = dfs(graph, 0)
    assert sorted(visited) == [0, 1]


# ---------------------------------------------------------------------------
# Dijkstra
# ---------------------------------------------------------------------------
def test_dijkstra_distances():
    distances, _ = dijkstra(WEIGHTED, 0)
    assert distances[0] == 0
    assert distances[1] == 3   # 0->2->1
    assert distances[2] == 1   # 0->2
    assert distances[3] == 4   # 0->2->1->3


def test_dijkstra_predecessors():
    _, predecessors = dijkstra(WEIGHTED, 0)
    assert predecessors[0] is None
    assert predecessors[2] == 0
    assert predecessors[1] == 2
    assert predecessors[3] == 1


def test_dijkstra_unreachable():
    graph = {0: [(1, 1)], 1: [], 2: [(3, 1)], 3: []}
    distances, _ = dijkstra(graph, 0)
    assert 2 not in distances
    assert 3 not in distances


# ---------------------------------------------------------------------------
# shortest_path
# ---------------------------------------------------------------------------
def test_shortest_path():
    dist, path = shortest_path(WEIGHTED, 0, 3)
    assert dist == 4
    assert path == [0, 2, 1, 3]


def test_shortest_path_no_path():
    graph = {0: [(1, 1)], 1: [], 2: []}
    dist, path = shortest_path(graph, 0, 2)
    assert path == []


# ---------------------------------------------------------------------------
# Prim MST
# ---------------------------------------------------------------------------
def test_prim_mst_weight():
    total, _ = prim_mst(UNDIRECTED_WEIGHTED)
    assert total == 16  # edges: (0,1,2),(1,2,3),(1,4,5),(0,3,6)


def test_prim_mst_edge_count():
    _, edges = prim_mst(UNDIRECTED_WEIGHTED)
    assert len(edges) == len(UNDIRECTED_WEIGHTED) - 1


def test_prim_mst_empty():
    total, edges = prim_mst({})
    assert total == 0
    assert edges == []


# ---------------------------------------------------------------------------
# Kruskal MST
# ---------------------------------------------------------------------------
KRUSKAL_NODES = [0, 1, 2, 3, 4]
KRUSKAL_EDGES = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9),
]


def test_kruskal_mst_weight():
    total, _ = kruskal_mst(KRUSKAL_NODES, KRUSKAL_EDGES)
    assert total == 16


def test_kruskal_mst_edge_count():
    _, edges = kruskal_mst(KRUSKAL_NODES, KRUSKAL_EDGES)
    assert len(edges) == len(KRUSKAL_NODES) - 1


def test_kruskal_mst_no_edges():
    total, edges = kruskal_mst([0, 1, 2], [])
    assert total == 0
    assert edges == []
