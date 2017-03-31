# done
# epi 17.10
# http://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0

def climbing_stairs(n, k):
    # n total steps, k at a time
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in xrange(1, n+1):
        current = 0
        for j in xrange(1, k + 1):
            if i-j >= 0:
                current += ways[i-j]
        ways[i] = current
    return ways[n]

print climbing_stairs(10, 1)
print climbing_stairs(10, 2)
print climbing_stairs(10, 3)
