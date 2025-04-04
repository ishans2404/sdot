def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]

# User input
nums = list(map(int, input("Enter house values separated by spaces: ").split()))
print("Maximum amount that can be robbed:", house_robber(nums))
