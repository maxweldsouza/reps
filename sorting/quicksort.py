
def quicksort(arr):
    def swap(left, right):
        if arr[left] != arr[right]:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    def qsort(left, right):
        if right - left < 1:
            return
        elif right - left == 1:
            if arr[left] > arr[right]:
                swap(left, right)
        else:
            pivot = left
            i = left + 1
            j = right
            while True:
                while i+1 <= right and arr[i] <= arr[pivot]:
                    i += 1
                while j-1 >= left and arr[j] >= arr[pivot]:
                    j -= 1
                if j <= i:
                    break
                else:
                    swap(i, j)
            swap(pivot, i-1)
            print arr
            qsort(left, i-1)
            qsort(i-1, right)
    qsort(0, len(arr) - 1)

quicksort([3,2,1])
