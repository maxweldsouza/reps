# ctci 2.7
from collections import defaultdict

def intersection(nodea, nodeb):
    seen = defaultdict(int)
    while nodea.next:
        seen[nodea] += 1
        nodea = nodea.next
    while nodeb.next
        if seen[nodeb]:
            return nodeb
        nodeb = nodeb.next
    # check ref and not value
