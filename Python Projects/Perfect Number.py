num=int(input())

total=0

for i in range(1,num):
    if(num%i)==0:
        total+=i
if total==num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")