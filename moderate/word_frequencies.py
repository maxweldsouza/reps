# ctci 16.2

from collections import defaultdict

def word_frequencies(book):
    words = defaultdict(int)
    for word in book:
        words[word] += 1
