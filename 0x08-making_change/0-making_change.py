#!/usr/bin/env python3
from typing import List
""" The coin change problem"""


def makeChange(coins: List[int], total: int) -> int:
    """
    Calculate the minimum number of coins needed to make a given total.

    Args:
        coins (list of int): The denominations of the coins available.
        total (int): The total amount of money to make change for.

    Returns:
        int: The minimum number of coins needed to make the total, or -1 if it
        is not possible.
    """
    if total <= 0:
        return 0

    # Initialize dp array with total + 1 (representing infinity)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Build the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] <= total else -1
