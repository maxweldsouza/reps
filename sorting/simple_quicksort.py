def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    same = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]
    return quicksort(less) + same + quicksort(more)

print quicksort([3, 7, 4, 7, 2, 7, 1, 2, 2, 1, 6])
