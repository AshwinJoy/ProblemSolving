def fact(n):
    if n==1:
        return n
    return n * fact(n-1)
    
num = int(input())
result = fact(num)
print(result)