num=input()

length=len(num)

total=0
for digit in num:
    total+=int(digit)**length
    
if total==int(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")