# Read the input array and integer k
arr = list(map(int, input().split(',')))
k = int(input())

arr.sort()

# Initialize variables to track the minimum unfairness and its corresponding subarray
min_unfairness = float('inf')
min_unfairness_subarray = []

# Iterate through the array to find the subarray with minimum unfairness
for i in range(len(arr) - k + 1):
    subarray = arr[i:i + k]
    current_unfairness = max(subarray) - min(subarray)
    if current_unfairness < min_unfairness:
        min_unfairness = current_unfairness
        min_unfairness_subarray = subarray

# Print the subarray with minimum unfairness
print(min_unfairness_subarray)
