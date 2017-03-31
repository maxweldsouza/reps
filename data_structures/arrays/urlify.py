# ctci 1.3
#done
def urlify(s):
    result = []
    for c in s:
        if c == ' ':
            result.append('%20')
        else:
            result.append(c)
    return ''.join(result)

assert urlify(' ') == '%20'
assert urlify('x x') == 'x%20x'
