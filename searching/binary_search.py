

def binary_search_help(arr, item, left, right):
    if left == right:
        return left
    mid = 1 + (left + right) / 2
    if item >= arr[mid]:
        return binary_search_help(arr, item, mid, right)
    elif item < arr[mid]:
        return binary_search_help(arr, item, left, mid-1)
    else:
        return mid

def binary_search(arr, item):
    return binary_search_help(arr, item, 0, len(arr) - 1)

print binary_search([2, 5, 5, 5, 7, 9, 10], 5)
