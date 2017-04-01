# epi 5.1
# done

def parity(x):
    print "{0:b}".format(x)
    result = 0
    while x:
        print x & 1, x >> 1
        result += (x & 1)
        x = x >> 1
    return result

print parity(1000)
