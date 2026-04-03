"""Optimized searching algorithms.

Includes:
- Binary Search       — O(log n) on sorted lists
- Interpolation Search — O(log log n) average for uniform distributions
"""

from typing import List, Optional


def binary_search(arr: List[int], target: int) -> int:
    """Search for *target* in a sorted list using binary search.

    Args:
        arr:    A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of *target* in *arr*, or -1 if not found.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def interpolation_search(arr: List[int], target: int) -> int:
    """Search for *target* in a sorted list using interpolation search.

    Performs best when values are uniformly distributed.

    Args:
        arr:    A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of *target* in *arr*, or -1 if not found.

    Time:  O(log log n) average for uniform distributions, O(n) worst case
    Space: O(1)
    """
    lo, hi = 0, len(arr) - 1

    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[lo] == arr[hi]:
            if arr[lo] == target:
                return lo
            return -1

        # Estimate position using linear interpolation
        pos = lo + ((target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1


def find_first_occurrence(arr: List[int], target: int) -> int:
    """Return the index of the *first* occurrence of *target* in a sorted list.

    Uses binary search to find the leftmost position.

    Args:
        arr:    A sorted list of integers (may contain duplicates).
        target: The value to search for.

    Returns:
        The index of the first occurrence of *target*, or -1 if not found.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def find_last_occurrence(arr: List[int], target: int) -> int:
    """Return the index of the *last* occurrence of *target* in a sorted list.

    Args:
        arr:    A sorted list of integers (may contain duplicates).
        target: The value to search for.

    Returns:
        The index of the last occurrence of *target*, or -1 if not found.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
