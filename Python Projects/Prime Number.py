n=int(input())
factor=0
for i in range(2,n):
    if(n%i==0):
        factor=factor+1
if factor==0:
    print("Prime Number")
else:
    print("Not a Prime Number")