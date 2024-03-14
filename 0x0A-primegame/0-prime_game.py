#!/usr/bin/python3

def SieveOfEratosthenes(n):
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


def getMaxMultiples(n, primes_number, exclude=[]):
    tmp_max = 0
    number = 0
    for i in primes_number:
        if exclude.count(i) > 0:
            continue
        total = int(n / i)
        for j in exclude:
            total -= int(n / (i * j))
        if total > tmp_max:
            number = i
            tmp_max = max(tmp_max, total)
    return number


def play(players, n, primes_numbers, exclude=[]):
    turn = 0
    while True:
        if turn == 0:
            x = getMaxMultiples(n, primes_numbers, exclude)
            if (x == 0):
                players[1] += 1
                return
            exclude.append(x)
        else:
            x = getMaxMultiples(n, primes_numbers, exclude)
            if (x == 0):
                players[0] += 1
                return
            exclude.append(x)
        turn = 1 - turn


def isWinner(x, nums):
    players = [0, 0]
    maxNum = max(nums)
    primes = SieveOfEratosthenes(maxNum)
    primes_numbers = [i for i in range(len(primes)) if primes[i]]
    for n in nums:
        exclude = []
        play(players, n, primes_numbers, exclude)
    if players[0] > players[1]:
        return "Maria"
    elif players[0] < players[1]:
        return "Ben"
    else:
        return None
