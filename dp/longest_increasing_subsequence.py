# works but is O(n^2)
# TODO O(n log n)
# http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
# http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# https://www.hackerrank.com/challenges/longest-increasing-subsequent
# http://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0

def longest_increasing_subsequence(arr):
    lis = [1] * len(arr)
    for i, x in enumerate(arr):
        for j in range(0, i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

print longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
