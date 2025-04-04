def trap_rain_water(height):
    if not height:
        return 0
    n = len(height)
    left, right = [0] * n, [0] * n
    left[0], right[n - 1] = height[0], height[n - 1]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - height[i]
    return water

# User input
height = list(map(int, input("Enter bar heights separated by spaces: ").split()))
print("Trapped Rain Water:", trap_rain_water(height))
