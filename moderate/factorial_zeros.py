# ctci 16.5
#done

def factorial_zeros(n):
    factorial = product([i for i in range(1, n+1)])
    r = reversed(str(factorial))
    count = 0
    for c in r:
        if c == '0':
            count += 1
        else:
            break
    return count

assert factorial_zeros(2) == 0
assert factorial_zeros(5) == 1
assert factorial_zeros(9) == 1
assert factorial_zeros(11) == 2
