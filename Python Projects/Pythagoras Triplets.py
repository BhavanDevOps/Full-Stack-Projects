L=int(input())
count=0
for a in range(1,L-1):
    for b in range(a+1,L):
        for c in range(b+1,L+1):
            x=a*a
            y=b*b
            z=c*c
            if (x+y==z):
                count+=1


print(count)