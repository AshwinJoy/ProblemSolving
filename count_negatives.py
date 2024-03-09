def countNegatives(grid, n, m):
    count = 0
    row, col = 0, m - 1  # Start from the top-right corner

    while row < n and col >= 0:
        if grid[row][col] < 0:
            count += col + 1  # Add remaining elements in the column
            row += 1  # Move down
        else:
            col -= 1 # Move to the left
            
    return count

# Read input
n = int(input())
m = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Calculate and print the result
print(countNegatives(grid, n, m))