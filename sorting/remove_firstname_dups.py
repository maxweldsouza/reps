# epi 14.4

def remove_dups(names):
    seen = {}
    result = []
    for first, last in names:
        if first not in seen:
            seen[first] = True
            result.append((first, last))
    return result

print remove_dups([('Ian', 'Botham'), ('David', 'Gower'), ('Ian', 'Bell'), ('Ian', 'Chappell')])
