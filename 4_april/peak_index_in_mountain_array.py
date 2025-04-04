def peak_index_in_mountain_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

# User input
arr = list(map(int, input("Enter mountain array separated by spaces: ").split()))
print("Peak index in mountain array:", peak_index_in_mountain_array(arr))
