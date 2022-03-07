a=int(input())
b=int(input())
c=int(input())

if (a==b==c):
    print("Equilateral")
elif (a==b) or (b==c):
    print("Isosceles")
else:
    print("Scalene")