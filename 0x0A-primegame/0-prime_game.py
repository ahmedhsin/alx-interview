#!/usr/bin/python3
"""solution for prime game"""


def SieveOfEratosthenes(n):
    """seive of eratosthenes to find prime numbers till n"""
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p]):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime


def getFsmallest(n, primes_number, exclude=[]):
    """get max multiples of n from prime numbers excluding exclude list"""
    for i in primes_number:
        if exclude.count(i):
            continue
        return i
    return 0


def play(players, n, primes_numbers, exclude=[]):
    """play the game and update the players score"""
    turn = 0
    while True:
        if turn == 0:
            x = getFsmallest(n, primes_numbers, exclude)
            if (x == 0):
                players[1] += 1
                return
            exclude.append(x)
        else:
            x = getFsmallest(n, primes_numbers, exclude)
            if (x == 0):
                players[0] += 1
                return
            exclude.append(x)
        turn = 1 - turn


def isWinner(x, nums):
    """find the winner of the game"""
    if (x <= 0 or nums == [] or x != len(nums)):
        return None
    players = [0, 0]
    maxNum = max(nums)
    primes = SieveOfEratosthenes(maxNum + 10)
    for n in nums:
        exclude = []
        primesNUmberTilln = [i for i in range(n + 1) if primes[i]]
        play(players, n, primesNUmberTilln, exclude)
    if players[0] > players[1]:
        return "Maria"
    elif players[0] < players[1]:
        return "Ben"
    else:
        return None
