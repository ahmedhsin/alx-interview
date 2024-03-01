#!/usr/bin/python3
"""this is a solution fro coin change problem"""


def makeChange(coins, total):
    """will solved in iterative way"""
    dp = [-1 for _ in range(total+1)]
    a = coins.copy()
    coins.sort()
    coins.reverse()
    for i in range(total+1):
        if i == 0:
            dp[i] = 0
            continue
        for coin in coins:
            if coin > i:
                continue
            mn = 1 + dp[i-coin]
            if dp[i-coin] == -1:
                dp[i] = -1
            elif dp[i] == -1:
                dp[i] = mn
            else:
                dp[i] = min(mn, dp[i])
                break
    coins = a
    return (dp[total])
