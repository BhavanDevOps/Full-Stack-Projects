m=int(input())
n=int(input())

if m>n:
    smallest_number=n
else:
    smallest_number=m
gcd=smallest_number
for i in range(1,smallest_number+1):
    if((m%i)==0) and ((n%i)==0):
        gcd=i
print(gcd)