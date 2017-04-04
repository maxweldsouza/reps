def mergesort_help(arr, l, r):
    if r == l:
        return
    mid = (l + r) / 2
    mergesort_help(arr, l, mid)
    mergesort_help(arr, mid+1, r)
    i, j = l, mid+1
    merged = []
    while True:
        if i > mid:
            merged += arr[j:r+1]
            break
        if j > r:
            merged += arr[i:mid+1]
            break
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    for i, j in enumerate(xrange(l, r+1)):
        arr[j] = merged[i]
    return arr

def mergesort(arr):
    return mergesort_help(arr, 0, len(arr)-1)

print mergesort([3, 7, 4, 7, 2, 7, 1, 2, 2, 1, 6])
