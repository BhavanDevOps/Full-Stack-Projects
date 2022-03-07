def compute_factorial(n):
    if n<=0:
        return 1
    return n*compute_factorial(n-1)


num = int(input())
result=compute_factorial(num)
print(result)