"""Tests for searching algorithms."""

import pytest

from algorithms.searching import (
    binary_search,
    find_first_occurrence,
    find_last_occurrence,
    interpolation_search,
)

SORTED_LIST = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# ---------------------------------------------------------------------------
# Binary search
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "target,expected_idx",
    [
        (1, 0),
        (19, 9),
        (9, 4),
        (4, -1),
        (20, -1),
    ],
)
def test_binary_search(target, expected_idx):
    assert binary_search(SORTED_LIST, target) == expected_idx


def test_binary_search_empty():
    assert binary_search([], 5) == -1


def test_binary_search_single_match():
    assert binary_search([42], 42) == 0


def test_binary_search_single_no_match():
    assert binary_search([42], 7) == -1


# ---------------------------------------------------------------------------
# Interpolation search
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "target,expected_idx",
    [
        (1, 0),
        (19, 9),
        (9, 4),
        (4, -1),
        (0, -1),
        (20, -1),
    ],
)
def test_interpolation_search(target, expected_idx):
    assert interpolation_search(SORTED_LIST, target) == expected_idx


def test_interpolation_search_empty():
    assert interpolation_search([], 5) == -1


def test_interpolation_search_all_same():
    # All elements identical — should find or miss correctly
    assert interpolation_search([5, 5, 5], 5) == 0
    assert interpolation_search([5, 5, 5], 3) == -1


# ---------------------------------------------------------------------------
# First / last occurrence
# ---------------------------------------------------------------------------
DUP_LIST = [1, 2, 2, 2, 3, 4, 4, 5]


def test_find_first_occurrence():
    assert find_first_occurrence(DUP_LIST, 2) == 1
    assert find_first_occurrence(DUP_LIST, 4) == 5
    assert find_first_occurrence(DUP_LIST, 6) == -1


def test_find_last_occurrence():
    assert find_last_occurrence(DUP_LIST, 2) == 3
    assert find_last_occurrence(DUP_LIST, 4) == 6
    assert find_last_occurrence(DUP_LIST, 6) == -1
