"""Optimized algorithms practice package."""

from .sorting import merge_sort, quick_sort, heap_sort, counting_sort
from .searching import binary_search, interpolation_search
from .dynamic_programming import fibonacci, knapsack_01, longest_common_subsequence, coin_change
from .graph import bfs, dfs, dijkstra, prim_mst, kruskal_mst

__all__ = [
    "merge_sort",
    "quick_sort",
    "heap_sort",
    "counting_sort",
    "binary_search",
    "interpolation_search",
    "fibonacci",
    "knapsack_01",
    "longest_common_subsequence",
    "coin_change",
    "bfs",
    "dfs",
    "dijkstra",
    "prim_mst",
    "kruskal_mst",
]
