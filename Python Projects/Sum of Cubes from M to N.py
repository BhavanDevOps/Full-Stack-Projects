def sum_of_cubes_m_to_n(m, n):
    # Complete this function
    total=0
    for i in range(m,n+1):
        total+=(i**3)
    return total
m = int(input())
n = int(input())
# Call the sum_of_cubes_m_to_n function
result=sum_of_cubes_m_to_n(m,n)
print(result)