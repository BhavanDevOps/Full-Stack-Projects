number=int(input())

total=1+number
for i in range(2,number):
    if(number%i)==0:
        total+=i
        
print(total)