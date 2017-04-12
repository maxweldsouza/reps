# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
# https://www.hackerrank.com/challenges/coin-change

def coin_change_dp(coins, amount):
    table = [[1 if i == 0 else 0 for i in range(amount + 1)] for j in coins]
    for i, coin in enumerate(coins):
        for s in range(amount + 1):
            including = table[i][s-coin] if s-coin >=0 else 0
            excluding = table[i-1][s]
            table[i][s] = including + excluding
    return table[-1][-1]

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

print coin_change_dp([1, 2, 3], 4)
