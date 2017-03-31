# ctci 16.16

def sub_sort(a):
    i = len(a) - 1
    smallest = a[-1]
    m = 0
    while i >= 0:
        if a[i] <= smallest:
            smallest = a[i]
        else:
            m = 0
    largest = a[0]
    n = len(a) - 1
    i = 0
    while i < len(a):
        if a[i] >= largest:
            largest = a[i]
            n += 1
        else:
            n = 0

print sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
