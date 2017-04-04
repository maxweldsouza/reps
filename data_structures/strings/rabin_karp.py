# done
# epi 7.14

def rolling_hash (s):
    result = 0
    for i, c in enumerate(s):
        result += ord(c) * 2**i
    return result

def rabin_karp(search, text):
    ls = len(search)
    lt = len(text)
    if lt < ls:
        return False
    hsh = rolling_hash(search)
    i = 0
    match = rolling_hash(text[:ls])
    while i < lt - ls + 1:
        if match == hsh and text[i:i+ls] == search:
            return i
        if i + ls < len(text):
            match -= ord(text[i])
            match /= 2
            match += ord(text[i + ls]) * 2**(ls-1)
        i += 1
    return False

print rabin_karp ('over', 'the quick brown fox jumps over the lazy dog')
print rabin_karp ('dog', 'the quick brown fox jumps over the lazy dog')
print rabin_karp ('the', 'the quick brown fox jumps over the lazy dog')
print rabin_karp ('dag', 'the quick brown fox jumps over the lazy dog')
