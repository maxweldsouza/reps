# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

cache = {}
def coin_change(coins, amount):
    if (coins, amount) in cache:
        return cache[(coins, amount)]

    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(coins) == 0:
        return 0

    result = coin_change(coins, amount - coins[0]) + coin_change(coins[1:], amount)
    cache[(coins, amount)] = result
    return result

print coin_change([1, 2, 3], 4)
