def fibonacci(n):
    # Complete this function
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n = int(input())
# call the fibonacci function
result=fibonacci(n)
print(result)
