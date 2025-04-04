import math

def min_deletions(nums, numsDivide):
    nums.sort()
    g = math.gcd(*numsDivide)
    for i, num in enumerate(nums):
        if g % num == 0:
            return i
    return -1

# User input
nums = list(map(int, input("Enter the first array separated by spaces: ").split()))
numsDivide = list(map(int, input("Enter the second array separated by spaces: ").split()))
result = min_deletions(nums, numsDivide)
if result == -1:
    print("It's not possible to make the array divisible.")
else:
    print("Minimum deletions required:", result)
