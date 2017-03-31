# ctci 1.2
# done
from collections import defaultdict

def compare_default_dicts(a, b):
    if len(a) != len(b):
        return False
    for key, value in a.iteritems():
        if a[key] != b[key]:
            return False
    return True

def permutation(a, b):
    da = defaultdict(int)
    db = defaultdict(int)
    for c in a:
        da[c] += 1
    for c in b:
        db[c] += 1
    return compare_default_dicts(da, db)

assert permutation('a', 'a')
assert permutation('ba', 'ab')
assert not permutation('a', 'ac')
