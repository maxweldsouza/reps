# ctci 1.6
#done

def string_compress(s):
    prev = s[0]
    result = []
    count = 0
    for c in s:
        if c == prev:
            count += 1
        else:
            result.append(prev)
            result.append(str(count))
            count = 1
        prev = c
    result.append(prev)
    result.append(str(count))
    compressed = ''.join(result)
    if len(compressed) >= len(s):
        return s
    else:
        return compressed

assert string_compress('aaabb') == 'a3b2'
assert string_compress('abc') == 'abc'
