"""Dynamic programming algorithms.

Includes:
- Fibonacci           — O(n) memoized / O(1) space iterative
- 0/1 Knapsack        — O(n * W)
- Longest Common Subsequence — O(m * n)
- Coin Change         — O(amount * len(coins))
"""

from typing import List, Tuple


def fibonacci(n: int) -> int:
    """Return the *n*-th Fibonacci number (0-indexed, F(0)=0, F(1)=1).

    Uses the iterative bottom-up approach.

    Args:
        n: Non-negative integer.

    Returns:
        The *n*-th Fibonacci number.

    Raises:
        ValueError: if *n* is negative.

    Time:  O(n)
    Space: O(1)
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def knapsack_01(
    weights: List[int], values: List[int], capacity: int
) -> Tuple[int, List[int]]:
    """Solve the 0/1 knapsack problem with dynamic programming.

    Args:
        weights:  List of item weights (non-negative integers).
        values:   List of item values (non-negative integers).
        capacity: Maximum weight the knapsack can carry.

    Returns:
        A tuple (max_value, selected_items) where *selected_items* is a list
        of 0-based indices of the chosen items.

    Raises:
        ValueError: if *weights* and *values* have different lengths.

    Time:  O(n * W)
    Space: O(n * W)
    """
    n = len(weights)
    if len(values) != n:
        raise ValueError("weights and values must have the same length.")

    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i = weights[i - 1]
        v_i = values[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if w_i <= w and dp[i - 1][w - w_i] + v_i > dp[i][w]:
                dp[i][w] = dp[i - 1][w - w_i] + v_i

    # Backtrack to find which items were selected
    selected: List[int] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()

    return dp[n][capacity], selected


def longest_common_subsequence(s1: str, s2: str) -> Tuple[int, str]:
    """Find the longest common subsequence of two strings.

    Args:
        s1: First string.
        s2: Second string.

    Returns:
        A tuple (length, lcs_string) where *length* is the LCS length and
        *lcs_string* is one such subsequence.

    Time:  O(m * n)
    Space: O(m * n)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the subsequence
    lcs_chars: List[str] = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs_chars.reverse()

    return dp[m][n], "".join(lcs_chars)


def coin_change(coins: List[int], amount: int) -> int:
    """Return the minimum number of coins needed to make *amount*.

    Args:
        coins:  List of available coin denominations (positive integers).
        amount: Target amount (non-negative integer).

    Returns:
        The fewest number of coins needed, or -1 if the amount cannot be made.

    Time:  O(amount * len(coins))
    Space: O(amount)
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1

    return int(dp[amount]) if dp[amount] != INF else -1
