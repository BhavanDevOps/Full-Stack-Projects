n=int(input())

for i in range(1,n+1):
    zeroes="0 "*(n-i)
    ones="1 "*((2*i)-1)
    print(zeroes+ones+zeroes)