"""Tests for sorting algorithms."""

import pytest

from algorithms.sorting import (
    counting_sort,
    heap_sort,
    merge_sort,
    quick_sort,
)

# ---------------------------------------------------------------------------
# Shared test cases
# ---------------------------------------------------------------------------
SORT_CASES = [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([3, 3, 1, 2, 1], [1, 1, 2, 3, 3]),
    (list(range(100, 0, -1)), list(range(1, 101))),
]


@pytest.mark.parametrize("arr,expected", SORT_CASES)
def test_merge_sort(arr, expected):
    assert merge_sort(arr) == expected


@pytest.mark.parametrize("arr,expected", SORT_CASES)
def test_quick_sort(arr, expected):
    assert quick_sort(arr) == expected


@pytest.mark.parametrize("arr,expected", SORT_CASES)
def test_heap_sort(arr, expected):
    assert heap_sort(arr) == expected


@pytest.mark.parametrize("arr,expected", SORT_CASES)
def test_counting_sort(arr, expected):
    assert counting_sort(arr) == expected


def test_counting_sort_raises_on_negatives():
    with pytest.raises(ValueError):
        counting_sort([-1, 2, 3])


def test_sort_does_not_mutate_input():
    original = [3, 1, 2]
    arr = original[:]
    merge_sort(arr)
    quick_sort(arr)
    heap_sort(arr)
    assert arr == original
