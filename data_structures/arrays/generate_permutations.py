
# epi 6.11
# http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

# duplicates are not allowed
def permutations(arr):
    while True:
        arr = arr[:]
        i = len(arr) - 1
        while i > 0 and arr[i] < arr[i-1]:
            i -= 1
        if i == 0:
            break
        j = len(arr) - 1
        while j > i and arr[j] < arr[i-1]:
            j -= 1
        arr[i-1], arr[j] = arr[j], arr[i-1]
        arr = arr[:i+1] + list(reversed(arr[i+1:]))
        yield arr

print list(permutations([2, 4, 5, 3]))
