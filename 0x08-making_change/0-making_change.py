#!/usr/bin/python3
'''0-making_change module'''


def makeChange(coins, total):
    '''Given a pile of coins of different values,
    determine the fewest number of coins needed to
    meet a given amount total
    '''

    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    number = 0
    for coin in coins:
        if total > 0:
            number += total // coin
            total = total % coin
    if total > 0:
        return -1
    else:
        return number