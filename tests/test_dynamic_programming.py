"""Tests for dynamic programming algorithms."""

import pytest

from algorithms.dynamic_programming import (
    coin_change,
    fibonacci,
    knapsack_01,
    longest_common_subsequence,
)


# ---------------------------------------------------------------------------
# Fibonacci
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
        (20, 6765),
    ],
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)


# ---------------------------------------------------------------------------
# Knapsack 0/1
# ---------------------------------------------------------------------------
def test_knapsack_basic():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_val, items = knapsack_01(weights, values, capacity)
    assert max_val == 7  # items 0 (w=2,v=3) + 1 (w=3,v=4)
    assert set(items) == {0, 1}


def test_knapsack_zero_capacity():
    max_val, items = knapsack_01([1, 2], [10, 20], 0)
    assert max_val == 0
    assert items == []


def test_knapsack_empty():
    max_val, items = knapsack_01([], [], 10)
    assert max_val == 0
    assert items == []


def test_knapsack_length_mismatch_raises():
    with pytest.raises(ValueError):
        knapsack_01([1, 2], [10], 5)


def test_knapsack_selected_items_within_capacity():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    max_val, items = knapsack_01(weights, values, capacity)
    assert max_val == 9  # items 1 (w=3,v=4) + 2 (w=4,v=5)
    assert sum(weights[i] for i in items) <= capacity
    assert sum(values[i] for i in items) == max_val


# ---------------------------------------------------------------------------
# Longest Common Subsequence
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "s1,s2,length,lcs",
    [
        ("ABCBDAB", "BDCABA", 4, "BCBA"),
        ("AGGTAB", "GXTXAYB", 4, "GTAB"),
        ("", "ABC", 0, ""),
        ("ABC", "", 0, ""),
        ("ABC", "ABC", 3, "ABC"),
        ("ABC", "DEF", 0, ""),
    ],
)
def test_lcs(s1, s2, length, lcs):
    result_len, result_lcs = longest_common_subsequence(s1, s2)
    assert result_len == length
    assert result_lcs == lcs


# ---------------------------------------------------------------------------
# Coin Change
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "coins,amount,expected",
    [
        ([1, 5, 10, 25], 30, 2),   # 25 + 5
        ([1, 2, 5], 11, 3),        # 5 + 5 + 1
        ([2], 3, -1),              # impossible
        ([1], 0, 0),               # zero amount
        ([1, 5, 10], 0, 0),
        ([186, 419, 83, 408], 6249, 20),
    ],
)
def test_coin_change(coins, amount, expected):
    assert coin_change(coins, amount) == expected
