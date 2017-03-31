# ctci 17.11
# minimum distance

d = {}
for i, word in enumerate(file):
    if word in d:
        d[word].append(i)
    else:
        d[word] = [i]

for k, v in d.iteritems():
    d[k] = sorted(v)

def shortest_distance(word1, word2):
    try:
        a = d[word1]
        b = d[word2]
        i = 0
        j = 0
        min_distance = abs(a[0] - b[0])
        while i < len(a) and j < len(b):
            distance = abs(a[i] - b[j])
            if distance < min_distance:
                min_distance = distance
            if a[i] > b[j]:
                j += 1
            else:
                i += 1
        return min_distance
    except KeyError:
        return None
