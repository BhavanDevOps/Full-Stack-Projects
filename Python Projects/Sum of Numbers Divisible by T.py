given_number=int(input())
m=int(input())
n=int(input())

total=0
for number in range(m,n+1):
    if (number%given_number)==0:
        total+=number
print(total)