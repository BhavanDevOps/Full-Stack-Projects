n=int(input())

for i in range(1,n+1):
    left_spaces=" "*(n-i)
    if(i>2)and(i<n):
        hollow_spaces=" "*(2*(i-2))
        numbers="1 "+hollow_spaces+(str(i)+" ")
        print(left_spaces+numbers)
    else:
        numbers=""
        for j in range(1,i+1):
            numbers=numbers+(str(j)+" ")
        print(left_spaces+numbers)