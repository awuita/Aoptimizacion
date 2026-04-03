"""Optimized sorting algorithms.

Includes:
- Merge Sort  — O(n log n) stable sort
- Quick Sort  — O(n log n) average, in-place
- Heap Sort   — O(n log n) worst-case, in-place
- Counting Sort — O(n + k) for integer keys
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Sort *arr* using merge sort and return a new sorted list.

    Time:  O(n log n)
    Space: O(n)
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """Sort *arr* using quick sort and return a new sorted list.

    Uses the median-of-three pivot strategy to avoid worst-case O(n²)
    on already-sorted input.

    Time:  O(n log n) average, O(n²) worst case
    Space: O(log n) average stack depth
    """
    result = arr[:]
    _quick_sort_inplace(result, 0, len(result) - 1)
    return result


def _median_of_three(arr: List[int], lo: int, hi: int) -> int:
    mid = (lo + hi) // 2
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    # Place pivot at hi - 1
    arr[mid], arr[hi - 1] = arr[hi - 1], arr[mid]
    return arr[hi - 1]


def _quick_sort_inplace(arr: List[int], lo: int, hi: int) -> None:
    if hi - lo < 2:
        if hi > lo and arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        return

    pivot = _median_of_three(arr, lo, hi)
    i, j = lo, hi - 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[hi - 1] = arr[hi - 1], arr[i]
    _quick_sort_inplace(arr, lo, i - 1)
    _quick_sort_inplace(arr, i + 1, hi)


def heap_sort(arr: List[int]) -> List[int]:
    """Sort *arr* using heap sort and return a new sorted list.

    Time:  O(n log n)
    Space: O(1) auxiliary
    """
    result = arr[:]
    n = len(result)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(result, i, n)

    # Extract elements one by one
    for end in range(n - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _sift_down(result, 0, end)

    return result


def _sift_down(arr: List[int], root: int, size: int) -> None:
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest


def counting_sort(arr: List[int]) -> List[int]:
    """Sort a list of non-negative integers using counting sort.

    Time:  O(n + k)  where k = max(arr)
    Space: O(k)

    Raises:
        ValueError: if *arr* contains negative integers.
    """
    if not arr:
        return []

    if min(arr) < 0:
        raise ValueError("counting_sort requires non-negative integers.")

    k = max(arr)
    counts = [0] * (k + 1)
    for val in arr:
        counts[val] += 1

    result: List[int] = []
    for val, cnt in enumerate(counts):
        result.extend([val] * cnt)
    return result
