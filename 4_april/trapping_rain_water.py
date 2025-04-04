def trap_rain_water(heights):
    if not heights:
        return 0
    n = len(heights)
    left, right = 0, n - 1
    max_water = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water

n = int(input())
heights = list(map(int, input().split()))
print(trap_rain_water(heights))