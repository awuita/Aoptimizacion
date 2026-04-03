"""Graph algorithms.

Uses an adjacency-list representation: a dict mapping each node to a list of
(neighbour, weight) pairs for weighted graphs, or a list of neighbours for
unweighted graphs.

Includes:
- BFS           — Breadth-first search, O(V + E)
- DFS           — Depth-first search, O(V + E)
- Dijkstra      — Single-source shortest paths, O((V + E) log V)
- Prim MST      — Minimum spanning tree (Prim), O((V + E) log V)
- Kruskal MST   — Minimum spanning tree (Kruskal), O(E log E)
"""

import heapq
from collections import deque
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Type aliases
# ---------------------------------------------------------------------------
Graph = Dict[int, List[int]]              # unweighted adjacency list
WeightedGraph = Dict[int, List[Tuple[int, int]]]  # {node: [(neighbour, weight)]}


# ---------------------------------------------------------------------------
# BFS
# ---------------------------------------------------------------------------
def bfs(graph: Graph, start: int) -> List[int]:
    """Traverse *graph* from *start* using breadth-first search.

    Args:
        graph: Unweighted adjacency list {node: [neighbours]}.
        start: Starting node.

    Returns:
        A list of nodes in the order they were visited.

    Time:  O(V + E)
    Space: O(V)
    """
    visited: List[int] = []
    seen = {start}
    queue: deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)

    return visited


# ---------------------------------------------------------------------------
# DFS
# ---------------------------------------------------------------------------
def dfs(graph: Graph, start: int) -> List[int]:
    """Traverse *graph* from *start* using iterative depth-first search.

    Args:
        graph: Unweighted adjacency list {node: [neighbours]}.
        start: Starting node.

    Returns:
        A list of nodes in the order they were visited.

    Time:  O(V + E)
    Space: O(V)
    """
    visited: List[int] = []
    seen: set = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        visited.append(node)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in seen:
                stack.append(neighbour)

    return visited


# ---------------------------------------------------------------------------
# Dijkstra
# ---------------------------------------------------------------------------
def dijkstra(
    graph: WeightedGraph, start: int
) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
    """Compute shortest paths from *start* using Dijkstra's algorithm.

    Args:
        graph: Weighted adjacency list {node: [(neighbour, weight)]}.
               All weights must be non-negative.
        start: Source node.

    Returns:
        A tuple (distances, predecessors) where:
        - *distances*    maps each reachable node to its shortest distance.
        - *predecessors* maps each node to its predecessor on the shortest path
          (None for the source node).

    Time:  O((V + E) log V)
    Space: O(V)
    """
    distances: Dict[int, int] = {start: 0}
    predecessors: Dict[int, Optional[int]] = {start: None}
    heap: List[Tuple[int, int]] = [(0, start)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        if dist_u > distances.get(u, float("inf")):
            continue

        for v, weight in graph.get(u, []):
            new_dist = dist_u + weight
            if new_dist < distances.get(v, float("inf")):
                distances[v] = new_dist
                predecessors[v] = u
                heapq.heappush(heap, (new_dist, v))

    return distances, predecessors


def shortest_path(
    graph: WeightedGraph, start: int, end: int
) -> Tuple[int, List[int]]:
    """Return the shortest path from *start* to *end* using Dijkstra.

    Args:
        graph: Weighted adjacency list.
        start: Source node.
        end:   Destination node.

    Returns:
        A tuple (distance, path) where *path* is the list of nodes from
        *start* to *end*. Returns (infinity, []) if no path exists.
    """
    distances, predecessors = dijkstra(graph, start)

    if end not in distances:
        return float("inf"), []  # type: ignore[return-value]

    path: List[int] = []
    node: Optional[int] = end
    while node is not None:
        path.append(node)
        node = predecessors.get(node)
    path.reverse()
    return distances[end], path


# ---------------------------------------------------------------------------
# Prim MST
# ---------------------------------------------------------------------------
def prim_mst(graph: WeightedGraph) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Compute a minimum spanning tree using Prim's algorithm.

    Args:
        graph: Weighted *undirected* adjacency list.  Every edge (u, v, w)
               must appear as both (v, w) in graph[u] and (u, w) in graph[v].

    Returns:
        A tuple (total_weight, edges) where *edges* is a list of
        (u, v, weight) triples that form the MST.

    Time:  O((V + E) log V)
    Space: O(V)
    """
    if not graph:
        return 0, []

    start = next(iter(graph))
    in_mst: set = set()
    heap: List[Tuple[int, int, int]] = [(0, start, -1)]  # (weight, node, parent)
    total_weight = 0
    mst_edges: List[Tuple[int, int, int]] = []

    while heap:
        weight, u, parent = heapq.heappop(heap)
        if u in in_mst:
            continue
        in_mst.add(u)
        if parent != -1:
            total_weight += weight
            mst_edges.append((parent, u, weight))
        for v, w in graph.get(u, []):
            if v not in in_mst:
                heapq.heappush(heap, (w, v, u))

    return total_weight, mst_edges


# ---------------------------------------------------------------------------
# Kruskal MST (with Union-Find)
# ---------------------------------------------------------------------------
class _UnionFind:
    def __init__(self, nodes: List[int]) -> None:
        self.parent = {n: n for n in nodes}
        self.rank: Dict[int, int] = {n: 0 for n in nodes}

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal_mst(
    nodes: List[int], edges: List[Tuple[int, int, int]]
) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Compute a minimum spanning tree using Kruskal's algorithm.

    Args:
        nodes: List of node identifiers.
        edges: List of (u, v, weight) triples.

    Returns:
        A tuple (total_weight, mst_edges) where *mst_edges* is a list of
        (u, v, weight) triples that form the MST.

    Time:  O(E log E)
    Space: O(V)
    """
    uf = _UnionFind(nodes)
    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst_edges: List[Tuple[int, int, int]] = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == len(nodes) - 1:
                break

    return total_weight, mst_edges
