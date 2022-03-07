num=int(input())

for i in range(1,num+1):
    pattern=""
    for j in range(1,i+1):
        pattern=pattern+(str(j)+" ")
        
    print(pattern)