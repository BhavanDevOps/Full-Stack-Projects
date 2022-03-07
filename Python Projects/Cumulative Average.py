n=int(input())

total=0
for i in range(1,n+1):
    number=int(input())
    total=total+number
    average=total/i
    print(round(average,3))