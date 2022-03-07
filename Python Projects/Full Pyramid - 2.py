n=int(input())

for i in range(1,n+1):
    left_Spaces=" "*(n-i)
    numbers=""
    for j in range(1,i+1):
        numbers=numbers+(str(j)+" ")
    print(left_Spaces+numbers)