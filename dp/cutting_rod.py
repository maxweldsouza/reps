cache = {}

def cutting_rod(lengths, prices, n):
    if n in cache:
        return cache[n]
    if n == 0:
        result = 0
    else:
        result = max([prices[i] + cutting_rod(lengths, prices, n-length) for i, length in enumerate(lengths) if n-length >= 0])
    cache[n] = result
    return result
print cutting_rod([1, 2, 3, 4, 5, 6, 7, 8], [3, 5, 8, 9, 10, 17, 17, 20], 8)
