# ctci 16.6

def smallest_difference(a, b):
    n = sorted(a)
    m = sorted(b)
    i = 0
    j = 0
    mindiff = None
    minpair = None
    while i < len(n) and j < len(m):
        diff = n[i] - m[j]
        if (mindiff and 0 < diff < mindiff) or (diff > 0):
            minpair = (n[i], m[j])
            mindiff = diff
        if diff > 0:
            j += 1
        else:
            i += 1
    return minpair

print smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])
