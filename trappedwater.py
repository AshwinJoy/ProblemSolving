def trap_water(heights):
    if not heights:
        return 0

    n = len(heights)
    water_trapped = 0
    stack = []

    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            bounded_height = min(heights[i], heights[stack[-1]]) - heights[top]
            water_trapped += distance * bounded_height

        stack.append(i)

    return water_trapped

heights = list(map(int, input().split(",")))
print(trap_water(heights))
