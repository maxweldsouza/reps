def bubblesort(arr):
    while True:
        swaps = False
        for i in xrange(len(arr)- 1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swaps = True
        if not swaps:
            break
    print arr

bubblesort([1, 4, 2, 1])
