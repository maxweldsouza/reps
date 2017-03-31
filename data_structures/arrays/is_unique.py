#done
# ctci 1.1
from collections import defaultdict

def is_unique(s):
    if len(s) > 256:
        return False
    chars = defaultdict(int)

    for c in s:
        chars[c] += 1
        if chars[c] > 1:
            return False
    return True

assert is_unique('')
assert not is_unique('aa')
assert not is_unique('baac')
assert is_unique('bac')
assert is_unique('b')
