def fibonacci(n):
    # Complete this function to return nth term in fibonacci series
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def get_fibonacci_series(n):
    # Complete this function to return list of n terms of fibonacci series
    fibonacci_series=[]
    for i in range(n):
        term=fibonacci(i)
        fibonacci_series.append(term)
    return fibonacci_series

n = int(input())
# Call the get_fibonacci_series function
result=get_fibonacci_series(n)
print(result)
