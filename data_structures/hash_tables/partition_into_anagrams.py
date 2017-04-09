# epi 13.1

def partition(arr):
    anagrams = {}
    for word in arr:
        s = ''.join(sorted(word))
        if s in anagrams:
            anagrams[s].append(word)
        else:
            anagrams[s] = [word]
    return [group for group in anagrams.values() if len(group) > 1]

print partition(['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money'])
