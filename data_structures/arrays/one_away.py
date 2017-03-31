# ctci 1.5
#done

def one_away(x, y):
    if len(x) > len(y):
        a = x
        b = y
    else:
        b = x
        a = y

    if abs (len(a) - len(b)) == 1:
        deletions = 0
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] != b[j]:
                if deletions == 1:
                    return False
                else:
                    deletions += 1
                    i += 1
                    continue
            else:
                i += 1
                j += 1
        return deletions <= 1
    elif len(a) == len(b):
        differences = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                differences += 1
        return differences <= 1

assert one_away('pale', 'ple')
assert one_away('pales', 'pale')
assert one_away('pale', 'bale')
assert not one_away('pale', 'bake')
