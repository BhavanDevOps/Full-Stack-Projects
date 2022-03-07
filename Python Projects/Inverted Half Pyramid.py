num=int(input())

for i in range(num):
    pattern=""
    k=num-i
    for j in range(1,k+1):
        pattern=pattern+(str(j)+" ")
    print(pattern)