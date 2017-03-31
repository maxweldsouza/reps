# ctci 1.4
#done

from collections import defaultdict

def palindrome_permutation(s):
    counts = defaultdict(int)
    for c in counts:
        counts[c.lower()] += 1
    odds = 0
    for key, value in counts.iteritems():
        if value % 2 != 0 and value != ' ':
            odds += 1
    return (len(s) % 2 == 0 and odds == 0) or (len(s) % 2 != 0 and odds == 1)

assert palindrome_permutation('Tact coa')
assert not palindrome_permutation('Tat coa')
