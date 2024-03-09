towers = list(map(int,input().split(",")))
stack = []
n = len(towers)
water_trapped = 0

for i in range(n):
    while( len(stack)!=0 and (towers[i] > towers[stack[-1]]) ):
        popped_height = towers[stack[-1]]
        stack.pop()
        if len(stack) == 0:
            break
        distance = i - stack[-1] - 1
        min_height = min(towers[stack[-1]],towers[i]) - popped_height
        water_trapped += distance * min_height
    stack.append(i)
print(water_trapped)
