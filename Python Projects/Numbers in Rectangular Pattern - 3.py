m=int(input())
n=int(input())
number=1
for i in range(m):
    pattern=""
    for j in range(n):
        pattern=pattern+(str(number)+" ")
        number+=1
    print(pattern)