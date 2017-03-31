# ctci 17.7

from collections import defaultdict

def baby_names(frequencies, synonyms):
    groups = []
    d = {}

    for x, y in synonyms:
        if x not in d and y in d:
            groups[d[y]].append(x)
            d[x] = d[y]
        elif x in d and y not in d:
            groups[d[x]].append(y)
            d[y] = d[x]
        elif x not in d and y not in d:
            groups.append([x, y])
            d[x] = len(groups) - 1
            d[y] = d[x]
        else:
            groups[d[x]].extend(groups[d[y]])
            groups[d[y]] = []
            d[y] = d[x]

    result = defaultdict(int)
    for group in groups:
        if len(group) > 0:
            total = 0
            for item in group:
                try:
                    total += frequencies[item]
                except KeyError:
                    continue
            name = group[0]
            result[name] = total

    return result

print baby_names({'John':15, 'Jon':12, 'Chris':13, 'Kris':4, 'Christopher':19}, [('Jon', 'John'), ('John', 'Johnny'), ('Chris', 'Kris'), ('Chris', 'Christopher')])
