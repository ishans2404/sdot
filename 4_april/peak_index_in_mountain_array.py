def find_peak(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left 

def binary_search(arr, target, left, right, ascending=True):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if ascending:
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def find_in_mountain_array(arr, target):
    peak = find_peak(arr)
    index = binary_search(arr, target, 0, peak, True)
    if index != -1:
        return index
    return binary_search(arr, target, peak + 1, len(arr) - 1, False)

# def find_in_mountain_array(arr, target):
#     for i, num in enumerate(arr):
#         if num == target:
#             return i
#     return -1

n = int(input())
mountain_arr = list(map(int, input().split()))
target = int(input())
res = find_in_mountain_array(mountain_arr, target)
print(res)