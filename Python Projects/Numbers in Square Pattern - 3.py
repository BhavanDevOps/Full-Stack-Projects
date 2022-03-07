n=int(input())
number=1
for i in range(n):
    pattern=""
    for j in range(n):
        pattern=pattern+(str(number)+" ")
        number+=1
    print(pattern)