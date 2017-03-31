# ctci 16.18
def get_a_and_b(s, pattern, i, j):
    a = ''
    b = ''
    for n, c in enumerate(pattern):
        if c == 'a':
            a = s[n-1:n+i+1]
        elif c == 'b':
            b = s[n-1:n+j+1]

    return (a, b)

def generate(pattern, a, b):
    for c in pattern:
        if c == 'a':
            for x in a:
                yield x
        elif c == 'b':
            for x in b:
                yield x

def match(s, pattern, a, b):
    for x, y in zip(s, generate(pattern, a, b)):
        if x != y:
            return False
    return True

def pattern_match(s, pattern):
    l = len(s)
    al = sum([1 for a in s if a == 'a'])
    bl = sum([1 for b in s if b == 'b'])

    for i in range(1, l):
        for j in range(1, l):
            if i * al + j * bl == len(pattern):
                a, b = get_a_and_b(s, pattern, i, j)

                if match(s, pattern, a, b):
                    return True
    return False

#print pattern_match('max', 'a')
#print pattern_match('maxmax', 'aa')
#print pattern_match('maxmax', 'bb')
print pattern_match('catcatgocatgo', 'aabab')
print pattern_match('catcatgocatgo', 'bbaba')
print not pattern_match('catcatgocatgo', 'aaba')
print not pattern_match('maxma', 'aa')
