# ctci 16.11

def diving_board(k, shorter, longer):
    i = 0
    while True:
        yield i * shorter + (k - i) * longer
        i += 1
