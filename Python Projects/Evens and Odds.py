def countodd(m,n):
    N=(n-m)//2
    if (n%2)!=0 or (m%2)!=0:
        N=N+1
    return N
m=int(input())
n=int(input())
odds=countodd(m,n)
evens=(n-m+1)-odds
print(odds)
print(evens)