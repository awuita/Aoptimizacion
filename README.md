# Aoptimizacion — Practica algoritmos optimizados

A collection of classic algorithms implemented in Python, with a focus on
time and space complexity.

## Algorithms

### Sorting (`algorithms/sorting.py`)
| Algorithm      | Time (avg)    | Space  | Stable |
|---------------|--------------|--------|--------|
| Merge Sort    | O(n log n)   | O(n)   | Yes    |
| Quick Sort    | O(n log n)   | O(log n)| No    |
| Heap Sort     | O(n log n)   | O(1)   | No     |
| Counting Sort | O(n + k)     | O(k)   | Yes    |

### Searching (`algorithms/searching.py`)
| Algorithm            | Time (avg)    | Space |
|---------------------|--------------|-------|
| Binary Search       | O(log n)     | O(1)  |
| Interpolation Search| O(log log n) | O(1)  |
| First/Last Occurrence | O(log n)   | O(1)  |

### Dynamic Programming (`algorithms/dynamic_programming.py`)
| Algorithm                   | Time           | Space  |
|-----------------------------|---------------|--------|
| Fibonacci                   | O(n)          | O(1)   |
| 0/1 Knapsack                | O(n × W)      | O(n × W)|
| Longest Common Subsequence  | O(m × n)      | O(m × n)|
| Coin Change                 | O(amount × k) | O(amount)|

### Graph (`algorithms/graph.py`)
| Algorithm       | Time             | Space |
|----------------|-----------------|-------|
| BFS            | O(V + E)        | O(V)  |
| DFS            | O(V + E)        | O(V)  |
| Dijkstra       | O((V+E) log V)  | O(V)  |
| Prim MST       | O((V+E) log V)  | O(V)  |
| Kruskal MST    | O(E log E)      | O(V)  |

## Usage

```python
from algorithms.sorting import merge_sort, quick_sort
from algorithms.searching import binary_search
from algorithms.dynamic_programming import fibonacci, knapsack_01
from algorithms.graph import bfs, dijkstra

# Sorting
sorted_list = merge_sort([5, 3, 1, 4, 2])   # [1, 2, 3, 4, 5]

# Searching
idx = binary_search([1, 3, 5, 7, 9], 7)     # 3

# Dynamic programming
fib = fibonacci(10)                          # 55
max_val, items = knapsack_01([2, 3, 4], [3, 4, 5], 5)

# Graph
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
order = bfs(graph, 0)                        # [0, 1, 2, 3]
```

## Running Tests

```bash
pip install pytest
pytest
```