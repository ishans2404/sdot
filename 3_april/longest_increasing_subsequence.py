def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

# User input
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Length of Longest Increasing Subsequence:", longest_increasing_subsequence(arr))
