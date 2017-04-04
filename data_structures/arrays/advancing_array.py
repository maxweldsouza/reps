# epi 6.4

def advancing(arr):
    rightmost = 0
    i = 0
    while i <= rightmost:
        print rightmost
        if arr[i] + i > rightmost:
            rightmost = arr[i] + i
        if i == len(arr) - 1:
            return True
        i += 1
    return False

assert advancing([1])
assert not advancing([0, 2])
assert advancing([1, 2])
assert advancing([4, 0, 0, 0, 0])
assert not advancing([3, 0, 0, 0, 0])
assert not advancing([3, 2, 0, 0, 2, 0, 1])
assert advancing([3, 3, 1, 0, 2, 0, 1])
