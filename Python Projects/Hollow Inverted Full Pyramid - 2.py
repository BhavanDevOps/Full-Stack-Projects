n=int(input())

for row in range(1,n+1):
    i=n-(row-1)
    left_spaces=" "*(row-1)
    if(i>2)and(i<n):
        hollow_spaces="  "*(i-2)
        numbers="1 "+hollow_spaces+(str(i)+" ")
        print(left_spaces+numbers)
    else:
        numbers=""
        for j in range(1,i+1):
            numbers=numbers+(str(j)+" ")
        print(left_spaces+numbers)