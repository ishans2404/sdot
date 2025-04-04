import math

def min_deletions(nums, numsDivide):
    nums.sort()
    g = math.gcd(*numsDivide)
    for i, num in enumerate(nums):
        if g % num == 0:
            return i
    return -1

nums = list(map(int, input().split()))
numsDivide = list(map(int, input().split()))
result = min_deletions(nums, numsDivide)
print(result)